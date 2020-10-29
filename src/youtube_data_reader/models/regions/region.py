from dataclasses import dataclass

from dataclasses_json import dataclass_json

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.regions.region_snippet import RegionSnippet


@dataclass_json
@dataclass
class Region(_IdentifiedModelBase):
    snippet: RegionSnippet
