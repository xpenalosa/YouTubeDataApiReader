from typing import Callable, Union, Any
from functools import wraps
import requests


class RequestErrorHandler:

    @staticmethod
    def handle_http_errors(func: Callable[[Union[Any]], requests.Response]) -> Callable[[Union[Any]], dict]:
        def is_error(code: int) -> bool:
            return code in [400, 401, 403, 404]

        def extract_error(response_body: dict) -> str:
            # TODO: parse [error][errors] and extract list of failure causes
            return response_body["error"]["message"]

        @wraps(func)
        def wrapper(*args, **kwargs) -> dict:
            response = func(*args, **kwargs)  # type: requests.Response
            body = response.json()  # type: dict
            if is_error(response.status_code):
                raise ValueError(extract_error(body))
            return body

        return wrapper
