from typing import Dict, Union, List

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoRegionRestriction:
    allowed: List[str]
    blocked: List[str]


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoContentDetails:
    caption: str
    content_rating: Dict[str, Union[str, List[str]]]
    definition: str
    dimension: str
    duration: str
    has_custom_thumbnail: bool
    licensed_content: bool
    projection: str
    region_restriction: VideoRegionRestriction
