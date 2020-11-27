import pytest


@pytest.fixture(scope="module")
def parts_validator():
    def validator(response_body, part_list):
        first_item = response_body["items"][0]  # type: dict
        for part in part_list:
            if first_item.get(part) is None:
                pytest.fail(f"'{part}' is not present in API response")
        return True

    return validator
