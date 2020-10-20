from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ModelBase:
    """Base model for all API responses"""
    kind: str  # Identifies the API resource's type.
    etag: str  # ETags allow applications to refer to a specific version of a particular API resource. Used for caching.
