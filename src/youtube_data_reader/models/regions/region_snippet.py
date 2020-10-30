from dataclasses_json import dataclass_json

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class RegionSnippet:
    """Dataclass for the Region 'snippet' part"""
    gl: str  # Two-letter ISO country code that identifies the region.
    name: str  # The name of the region
