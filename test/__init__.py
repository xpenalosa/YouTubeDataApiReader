import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def api_key():
    return os.environ.get("YT_API_KEY")
