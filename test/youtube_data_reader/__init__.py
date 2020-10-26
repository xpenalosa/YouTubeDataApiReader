import pytest
import os


@pytest.fixture(scope="session")
def api_key():
    return os.environ["YT_API_KEY"]
