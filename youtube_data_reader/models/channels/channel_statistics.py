from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class ChannelStatistics:
    hidden_subscriber_count: bool
    subscriber_count: int
    video_count: int
    view_count: int
