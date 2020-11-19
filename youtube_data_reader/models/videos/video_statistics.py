from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoStatistics:
    comment_count: int
    dislike_count: int
    favorite_count: int
    like_count: int
    view_count: int
