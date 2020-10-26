import requests
from urllib.parse import quote


class RequestHandler:
    domain = "https://www.googleapis.com/youtube/v3/"

    @staticmethod
    def _escape_parameters(parameters: dict) -> dict:
        return dict([(quote(k), quote(v)) for k, v in parameters.items()])

    @staticmethod
    def _form_parameter_string(parameters: dict) -> str:
        return "&".join([f"{k}={v}" for k, v in parameters.items()])

    @staticmethod
    def _build_url(domain: str, endpoint: str, parameters: dict) -> str:
        escaped_params = RequestHandler._escape_parameters(parameters)
        formatted_params = RequestHandler._form_parameter_string(escaped_params)
        return f"{domain}/{endpoint}?{formatted_params}"

    @staticmethod
    def request(endpoint, parameters: dict) -> requests.Response:
        url = RequestHandler._build_url(RequestHandler.domain, endpoint, parameters)
        return requests.get(url)
