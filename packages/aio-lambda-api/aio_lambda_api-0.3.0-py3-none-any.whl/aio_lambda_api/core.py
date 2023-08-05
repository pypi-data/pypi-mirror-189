"""API base."""
from asyncio import (
    new_event_loop as _new_event_loop,
    wait_for as _wait_for,
    gather as _gather,
)
from contextlib import AsyncExitStack as _AsyncExitStack
from inspect import signature as _signature
from typing import (
    Any as _Any,
    AsyncContextManager as _AsyncContextManager,
    TypeVar as _TypeVar,
    Dict as _Dict,
    Callable as _Callable,
    Iterable as _Iterable,
    Optional as _Optional,
    Coroutine as _Coroutine,
    Type as _Type,
    Tuple as _Tuple,
    List as _List,
)

try:
    from pydantic import validate_arguments as _validate_arguments
except ImportError:
    _validate_arguments = None  # type: ignore

from aio_lambda_api.exceptions import (
    HTTPException as _HttpException,
    ValidationError as _ValidationError,
)
from aio_lambda_api.responses import (
    Response as _Response,
    JSONResponse as _JSONResponse,
)
from aio_lambda_api.requests import Request as _Request
from aio_lambda_api.json import dumps as _dumps
from aio_lambda_api.logging import logger as _logger
from aio_lambda_api.settings import FUNCTION_TIMEOUT as _FUNCTION_TIMEOUT
from aio_lambda_api.backends import get_backend as _get_backend


_T = _TypeVar("_T")

_VALIDATOR_CONFIG = dict(arbitrary_types_allowed=True)


class _APIRoute:
    """API route."""

    __slots__ = ["status_code", "func", "params"]

    def __init__(
        self,
        func: _Callable[..., _Any],
        status_code: int,
        params: _Dict[str, _Type[_Any]],
    ) -> None:
        self.status_code = status_code
        self.func = func
        self.params = params


class Handler:
    """Serverless function handler."""

    __slots__ = ["_loop", "_exit_stack", "_routes", "_backend"]

    def __init__(self, backend: _Optional[str] = None) -> None:
        self._loop = _new_event_loop()
        self._exit_stack = _AsyncExitStack()
        self._routes: _Dict[str, _Dict[str, _APIRoute]] = dict()
        self._backend = _get_backend(backend)

    def __del__(self) -> None:
        self.run_async(self._exit_stack.__aexit__(None, None, None))

    def __call__(self, *args: _Any, **kwargs: _Any) -> _Any:
        """Entry point.

        Returns:
            Serialized response.
        """
        return self.run_async(self.__acall__(*args, **kwargs))

    async def __acall__(self, *args: _Any, **kwargs: _Any) -> _Any:
        """Async entry point.

        Returns:
            Serialized response.
        """
        parsed = await self._backend.parse_request(*args, **kwargs)
        if isinstance(parsed, _Request):
            return await self._backend.serialize_response(
                await self._handle_request(parsed), parsed
            )
        return await self._backend.serialize_responses(
            zip(await self._handle_requests(parsed), parsed)
        )

    async def _handle_requests(self, requests: _Iterable[_Request]) -> _List[_Response]:
        """Handle multiples requests.

        Args:
            requests: Requests.

        Returns:
            Responses.
        """
        return await _gather(*(self._handle_request(request) for request in requests))

    async def _handle_request(self, request: _Request) -> _Response:
        """Handle a single request.

        Args:
            request: Request.

        Returns:
            Response.
        """
        async with _logger(
            server=request.server_id, emit_log=self._backend.emit_log
        ) as log:
            try:
                log["method"] = request.method
                log["path"] = request.path

                response, func = await self._prepare_request(request)

                try:
                    log["request_id"] = request.headers["x-request-id"]
                except KeyError:
                    pass
                try:
                    log["user_agent"] = request.headers["user-agent"]
                except KeyError:
                    pass

                return await self._call_route_function(func, response)

            except _HttpException as exception:
                return self._handle_http_exception(exception, log)

            except _ValidationError as exception:
                errors = exception.errors()
                log["error_detail"] = _dumps(errors)
                log["status_code"] = 422
                log["level"] = "warning"
                return _JSONResponse(content=dict(detail=errors), status_code=422)

            except Exception as exception:
                response = self._handle_uncaught_exception(exception, log)
                if request.raises_exceptions:
                    raise
                return response

    async def _prepare_request(
        self, request: _Request
    ) -> _Tuple[_Response, _Coroutine[_Any, _Any, _Any]]:
        """Prepare the request.

        Args:
            request: Request.

        Returns:
            Default response object, Route function coroutine.
        """
        try:
            path_routes = self._routes[request.path]
        except KeyError:
            raise _HttpException(404)
        try:
            route = path_routes[request.method]
        except KeyError:
            raise _HttpException(405)

        response = _JSONResponse(status_code=route.status_code)

        body = await request.json()
        kwargs = body.copy() if isinstance(body, dict) else dict()
        for param_name, param_cls in route.params.items():
            if param_cls == _Request:
                kwargs[param_name] = request
            elif param_cls == _Response:
                kwargs[param_name] = response

        return response, route.func(**kwargs)

    async def _call_route_function(
        self, func: _Coroutine[_Any, _Any, _Any], response: _Response
    ) -> _Response:
        """Call the route function and returns its response.

        Args:
            func: Route function.
            response: Response.

        Returns:
            Response.
        """
        content = await _wait_for(func, _FUNCTION_TIMEOUT)
        if isinstance(content, _Response):
            response = content
        else:
            response.content = content
        return response

    def _handle_http_exception(
        self, exception: _HttpException, log: dict[str, _Any]
    ) -> _Response:
        """Handle HTTP exceptions.

        Args:
            exception: Exception to handle.
            log: Log.

        Returns:
            Response.
        """
        error_detail = exception.error_detail
        if error_detail:
            log["error_detail"] = error_detail
        log["status_code"] = exception.status_code
        if exception.status_code >= 500:
            log["level"] = "error"
        elif exception.status_code >= 400:
            log["level"] = "warning"
        return _JSONResponse(
            content=None if exception.detail is None else dict(detail=exception.detail),
            status_code=exception.status_code,
        )

    def _handle_uncaught_exception(
        self, exception: BaseException, log: dict[str, _Any]
    ) -> _Response:
        """Handle uncaught exceptions.

        Args:
            exception: Exception to handle.
            log: Log.

        Returns:
            Response.
        """
        log["level"] = "critical"
        http_exception = (self._backend.exception_hook(exception)) or _HttpException(
            500
        )
        log["status_code"] = http_exception.status_code
        if http_exception.error_detail:
            log["error_detail"] = http_exception.error_detail
        else:
            from traceback import format_exception

            log["error_detail"] = "".join(
                format_exception(type(exception), exception, exception.__traceback__)
            )
        return _JSONResponse(
            status_code=http_exception.status_code,
            content=http_exception.detail,
        )

    def enter_async_context(self, context: _AsyncContextManager[_T]) -> _T:
        """Initialize an async context manager.

        The context manager will be exited properly on API object destruction.

        Args:
            context: Async Object to initialize.

        Returns:
            Initialized object.
        """
        return self._loop.run_until_complete(
            self._exit_stack.enter_async_context(context)
        )

    def run_async(self, task: _Coroutine[_Any, _Any, _T]) -> _T:
        """Run an async task in the sync context.

        This can be used to call initialization functions outside the serverless
        function itself.

        Args:
            task: Async task.

        Returns:
            Task result.
        """
        return self._loop.run_until_complete(task)

    def _api_route(
        self,
        path: str,
        method: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register API route.

        Args:
            path: HTTP path.
            method: HTTP method.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """

        def decorator(func: _Callable[..., _Any]) -> _Callable[..., _Any]:
            """Decorator.

            Args:
                func: Route function.

            Returns:
                Route function.
            """
            params = self._check_signature(func)
            if _validate_arguments is not None:
                func = _validate_arguments(  # type: ignore
                    func, config=_VALIDATOR_CONFIG
                )
            try:
                path_routes = self._routes[path]
            except KeyError:
                path_routes = self._routes[path] = dict()
            try:
                path_routes[method]
            except KeyError:
                path_routes[method] = _APIRoute(
                    func=func, status_code=status_code or 200, params=params
                )
            else:
                raise ValueError(f'Route already registered: {method} "{path}".')
            return func

        return decorator

    @staticmethod
    def _check_signature(func: _Callable[..., _Any]) -> _Dict[str, _Type[_Any]]:
        """Check function signature and returns parameters to inject in functions calls.

        Args:
            func: Route function.

        Returns:
            Parameters to inject.
        """
        params: _Dict[str, _Type[_Any]] = dict()
        for param in _signature(func).parameters.values():
            annotation = param.annotation
            if isinstance(annotation, type) and issubclass(annotation, _Request):
                params[param.name] = _Request
            elif isinstance(annotation, type) and issubclass(annotation, _Response):
                params[param.name] = _Response
        return params

    def delete(
        self,
        path: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register a DELETE route.

        Args:
            path: HTTP path.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """
        return self._api_route(path=path, method="DELETE", status_code=status_code)

    def get(
        self,
        path: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register a GET route.

        Args:
            path: HTTP path.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """
        return self._api_route(path=path, method="GET", status_code=status_code)

    def head(
        self,
        path: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register a HEAD route.

        Args:
            path: HTTP path.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """
        return self._api_route(path=path, method="HEAD", status_code=status_code)

    def options(
        self,
        path: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register a OPTIONS route.

        Args:
            path: HTTP path.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """
        return self._api_route(path=path, method="OPTIONS", status_code=status_code)

    def patch(
        self,
        path: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register a PATCH route.

        Args:
            path: HTTP path.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """
        return self._api_route(path=path, method="PATCH", status_code=status_code)

    def post(
        self,
        path: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register a POST route.

        Args:
            path: HTTP path.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """
        return self._api_route(path=path, method="POST", status_code=status_code)

    def put(
        self,
        path: str,
        *,
        status_code: _Optional[int] = None,
    ) -> _Callable[[_Callable[..., _Any]], _Callable[..., _Any]]:
        """Register a PUT route.

        Args:
            path: HTTP path.
            status_code: HTTP status code.

        Returns:
            Decorator.
        """
        return self._api_route(path=path, method="PUT", status_code=status_code)
