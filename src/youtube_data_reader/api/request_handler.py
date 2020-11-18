import json
from urllib.parse import urljoin

import requests

_DOMAIN = "https://www.googleapis.com/youtube/v3/"


def _extract_error(response_body: dict) -> str:
    """Parse the JSON response from a failed request to the Youtube Data API and extracts the error(s).

    Expects the body to contain an error API response.

    :param response_body: The JSON object to parse.
    :return: The error or list of errors found within the response body.
    """
    # Remove method and inline call?
    # Catch KeyError and raise custom error indicating unexpected response?
    return json.dumps(response_body["error"]["errors"])


def query_endpoint(endpoint, parameters: dict) -> dict:
    """Build and execute an HTTPS request against the Youtube Data API.

    :param endpoint: The endpoint to query.
    :param parameters: A dictionary containing all the parameters to pass with the request.
    :return: The JSON response from the API.
    :raises requests.exceptions.HTTPError: If the API answers with a 4xx or 5xx code.
    """
    response = requests.get(
        urljoin(_DOMAIN, endpoint),
        params=parameters,
    )
    body = response.json()  # type: dict
    if not response.ok:
        error_message = _extract_error(body)
        raise requests.exceptions.HTTPError(error_message)
    return body
