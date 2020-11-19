import json
from datetime import datetime, timezone, timedelta

import pytest
from dataclasses_json import dataclass_json

from youtube_data_reader.models.utils import iso8601_datetime_field, defaulted_dataclass


@dataclass_json()
@defaulted_dataclass
class DatetimeDataclassTest:
    dt: datetime = iso8601_datetime_field()


@pytest.mark.parametrize("dataclass_dict, expected_field_value", [
    ({"dt": "2020-01-01T00:00:00"}, datetime(2020, 1, 1, 0, 0, 0)),
    ({"other": 1}, None),
    ({}, None),
    ({"dt": "2020-01-01T00:00:00", "other": "2000-12-31T23:59:59"}, datetime(2020, 1, 1, 0, 0, 0)),
])
def test_defaulted_dataclass(dataclass_dict, expected_field_value):
    dtc_from_dict = DatetimeDataclassTest.from_dict(dataclass_dict, infer_missing=True)
    assert dtc_from_dict.dt == expected_field_value

    dt_json = json.dumps(dataclass_dict)
    dtc_from_json = DatetimeDataclassTest.from_json(dt_json, infer_missing=True)
    assert dtc_from_json.dt == expected_field_value


@pytest.mark.parametrize("dt_str, expected_datetime", [
    ("2020-01-01T00:00:00Z", datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)),
    ("2020-01-01T00:00:00+05:00", datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=5)))),
    ("2020-01-01T00:00:00-05:00", datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(-timedelta(hours=5)))),
    ("2020-01-01T00:00:00", datetime(2020, 1, 1, 0, 0, 0)),
    (None, None),
])
def test_iso8601_datetime_field(dt_str, expected_datetime):
    dt_dict = {"dt": dt_str}
    dtc = DatetimeDataclassTest.from_dict(dt_dict)
    assert dtc.dt == expected_datetime
