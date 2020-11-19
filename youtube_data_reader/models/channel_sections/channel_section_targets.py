from typing import List

from dataclasses_json import dataclass_json

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class ChannelSectionTargets:
    countries: List[str]
    languages: List[str]
    regions: List[str]
