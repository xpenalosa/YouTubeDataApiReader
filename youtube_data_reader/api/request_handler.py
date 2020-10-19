import requests
from urllib.parse import quote


class RequestHandler:
    url = "https://www.googleapis.com/youtube/v3/"

    @staticmethod
    def _escape_parameters(parameters: dict) -> dict:
        return dict([(quote(k), quote(v)) for k, v in parameters.items()])

    @staticmethod
    def _form_parameter_string(parameters: dict) -> str:
        return "&".join([f"{k}={v}" for k, v in parameters.items()])

    @staticmethod
    def request(endpoint, parameters: dict) -> requests.Response:
        escaped_params = RequestHandler._escape_parameters(parameters)
        formatted_params = RequestHandler._form_parameter_string(escaped_params)
        return requests.get(f"{RequestHandler.url}/{endpoint}?{formatted_params}")
