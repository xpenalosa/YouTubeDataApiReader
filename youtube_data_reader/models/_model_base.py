from dataclasses_json import dataclass_json

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class _ModelBase:
    """Base model for all API responses"""
    etag: str  # ETags allow applications to refer to a specific version of a particular API resource. Used for caching.
    kind: str  # Identifies the API resource's type.
