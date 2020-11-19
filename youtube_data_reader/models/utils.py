"""Utility functions that are used throughout the models module.

The functions in this module are required in order to implement missing or limiting functionalities related to the
dataclasses_json module.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Union

from dataclasses_json import config


def defaulted_dataclass(_cls=None, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False):
    """Dirty hack to initialize all unset dataclass fields to None and change their type to Optional.

    This is required to populate the API responses into the dataclass models without `dataclasses_json` throwing
    warnings on uninitialized fields. As of v0.5.2, there is no option to silence these warnings other than adding the
    Optional typing annotation to each and every field and initializing it. This does not contribute to the simplicity
    of a codebase and `dataclasses_json` has not been updated since July 28th 2020, so plans to fix this are unclear.
    https://github.com/lidatong/dataclasses-json/issues/217.

    ----- dataclasses.dataclass documentation below -----

    Returns the same class as was passed in, with dunder methods added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr is true, a __repr__() method is added. If order
    is true, rich comparison dunder methods are added. If unsafe_hash is true, a __hash__() method function is added. If
    frozen is true, fields may not be assigned to after instance creation.
    """

    def wrap(cls):
        for attr_name, attr_type in cls.__annotations__.items():
            # Add NoneType to acceptable values
            cls.__annotations__[attr_name] = Union[attr_type, None]
            if not hasattr(cls, attr_name):
                # No default value for the attribute, set None as default
                setattr(cls, attr_name, field(default=None))
        # Return dataclass-wrapped class
        return dataclass(cls, init=init, repr=repr, eq=eq, order=order, unsafe_hash=unsafe_hash, frozen=frozen)

    if _cls is None:
        return wrap
    return wrap(_cls)


def iso8601_datetime_field() -> field:
    """Instantiate a dataclass_json field with metadata to parse an ISO8601 datetime string.

    ---

    datetime.fromisoformat does not support ISO datetime strings ending with Z to indicate Zulu time (+0 GMT). The
    YouTube API uses the format **YYYY-MM-DDThh:mm:ss.sssZ** to represent the datetime objects. The simple fix is to
    strip the trailing Z from the datetime string and set the timezone to UTC (+00:00) to conform to the expected
    format.

    :return: A dataclass field that can encode and decode ISO8601 datetime strings. The created datetimes are UTC-based.
    """

    def iso8601_datetime_decoder(dt_str: str) -> Union[datetime, None]:
        if dt_str:
            return datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        return None

    return field(metadata=config(
        encoder=datetime.isoformat,
        decoder=iso8601_datetime_decoder
    ))
