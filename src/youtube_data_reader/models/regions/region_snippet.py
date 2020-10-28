from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RegionSnippet:
    """Dataclass for the Region 'snippet' part"""
    gl: str  # Two-letter ISO country code that identifies the region.
    name: str  # The name of the region
