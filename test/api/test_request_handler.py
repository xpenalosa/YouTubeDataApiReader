import json

import pytest
from requests.exceptions import HTTPError

# noinspection PyUnresolvedReferences
from test import api_key
from youtube_data_reader.api.request_handler import query_endpoint


def test_extract_error():
    with pytest.raises(HTTPError) as exc_info:
        # No API key will raise authorization error
        query_endpoint("i18nLanguages", {})
    exceptions = json.loads(exc_info.value.args[0])
    assert exceptions[0]["message"] == "The request is missing a valid API key."
    assert exceptions[0]["reason"] == "forbidden"


@pytest.mark.skipif("not api_key")
def test_query_endpoint(api_key):
    response_body = query_endpoint("i18nLanguages", {"key": api_key})
    assert response_body is not None
    assert response_body.get("kind") == "youtube#i18nLanguageListResponse"
    assert response_body.get("etag") is not None
    assert len(response_body.get("items")) > 0
