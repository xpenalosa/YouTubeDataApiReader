from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoLiveStreamingDetails:
    active_live_chat_id: str
    actual_end_time: str  # FIXME: datetime
    actual_start_time: str  # FIXME: datetime
    concurrent_viewers: int
    scheduled_end_time: str  # FIXME: datetime
    scheduled_start_time: str  # FIXME: datetime
