from dataclasses import dataclass

from dataclasses_json import dataclass_json

from youtube_data_reader.models.identified_model_base import IdentifiedModelBase
from youtube_data_reader.models.regions.region_snippet import RegionSnippet


@dataclass_json
@dataclass
class Region(IdentifiedModelBase):
    snippet: RegionSnippet
