import pytest

from youtube_data_reader.api.request_handler import RequestHandler


@pytest.mark.parametrize(
    "param_dict, expected",
    [
        pytest.param({"key": "string"}, {"key": "string"}, id="Single key"),
        pytest.param({"key1": "string", "key2": "string"}, {"key1": "string", "key2": "string"}, id="Multiple keys"),
        pytest.param({"key": "?"}, {"key": "%3F"}, id="Single key (encoding required)"),
        pytest.param({"key1": "?", "key2": "à", "key3": "a"}, {"key1": "%3F", "key2": "%C3%A0", "key3": "a"},
                     id="Multiple keys (encoding required)"),
        pytest.param({}, {}, id="Empty"),
    ]
)
def test_escape_parameters(param_dict, expected):
    escaped = RequestHandler._escape_parameters(param_dict)
    assert escaped == expected


@pytest.mark.parametrize(
    "param_dict, expected",
    [
        pytest.param({"key": "value"}, "key=value", id="Single key"),
        pytest.param({"key1": "value1", "key2": "value2"}, "key1=value1&key2=value2", id="Multiple keys"),
        pytest.param({}, "", id="Empty")
    ]
)
def test_form_parameter_string(param_dict, expected):
    parameter_string = RequestHandler._form_parameter_string(param_dict)
    assert parameter_string == expected


@pytest.mark.parametrize(
    "domain, endpoint, param_dict, expected",
    [
        pytest.param("example.com", "e1", {"key": "value"}, "example.com/e1?key=value", id="Single key"),
        pytest.param("example.com", "e2", {"p1": "v1", "p2": "?"}, "example.com/e2?p1=v1&p2=%3F", id="Multiple keys"),
        pytest.param("example.com", "e3", {}, "example.com/e3?", id="Empty"),
    ]
)
def test_build_url(domain, endpoint, param_dict, expected):
    url = RequestHandler._build_url(domain, endpoint, param_dict)
    assert url == expected
