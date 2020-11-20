import os

import pytest


@pytest.fixture(scope="session")
def api_key():
    key = os.environ.get("YT_API_KEY")
    if not key:
        pytest.skip()
    return key
