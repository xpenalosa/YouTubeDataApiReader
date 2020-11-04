import json
from urllib.parse import urljoin

import requests


class RequestHandler:
    """HTTP request builder for the Youtube Data API."""

    DOMAIN = "https://www.googleapis.com/youtube/v3/"

    @staticmethod
    def extract_error(response_body: dict) -> str:
        # Remove method and inline call?
        return json.dumps(response_body["error"]["errors"])

    @staticmethod
    def query_endpoint(endpoint, parameters: dict) -> dict:
        response = requests.get(
            urljoin(RequestHandler.DOMAIN, endpoint),
            params=parameters,
        )
        body = response.json()  # type: dict
        if not response.ok:
            error_message = RequestHandler.extract_error(body)
            raise requests.exceptions.HTTPError(error_message)
        return body
