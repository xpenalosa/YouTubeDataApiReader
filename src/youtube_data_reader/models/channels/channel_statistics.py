from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelStatistics:
    hidden_subscriber_count: bool
    subscriber_count: int
    video_count: int
    view_count: int
