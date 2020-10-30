from dataclasses import dataclass, field as dc_field
from typing import Union


def defaulted_dataclass(_cls=None, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False):
    """Dirty hack to initialize all unset dataclass fields to None and change their type to Optional.

    This is required to populate the API responses into the dataclass models without `dataclasses_json` throwing
    warnings on uninitialized fields. As of v0.5.2, there is no option to silence these warnings other than adding the
    Optional typing annotation to each and every field and initializing it. This does not contribute to the simplicity
    of a codebase and `dataclasses_json` has not been updated for 3 months, so plans to fix this are unclear.
    https://github.com/lidatong/dataclasses-json/issues/217.

    ----- dataclasses.dataclass documentation below -----

    Returns the same class as was passed in, with dunder methods added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr is true, a __repr__() method is added. If order
    is true, rich comparison dunder methods are added. If unsafe_hash is true, a __hash__() method function is added. If
    frozen is true, fields may not be assigned to after instance creation.
    """

    def wrap(cls):
        for field, value in cls.__annotations__.items():
            # Add NoneType to acceptable values
            cls.__annotations__[field] = Union[value, None]
            if not hasattr(cls, field):
                # No default value for the field, set None as default
                setattr(cls, field, dc_field(default=None))
        # Return dataclass-wrapped class
        return dataclass(cls, init=init, repr=repr, eq=eq, order=order, unsafe_hash=unsafe_hash, frozen=frozen)

    if _cls is None:
        return wrap
    return wrap(_cls)
