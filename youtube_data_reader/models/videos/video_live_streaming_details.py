from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass, iso8601_datetime_field


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoLiveStreamingDetails:
    active_live_chat_id: str
    actual_end_time: datetime = iso8601_datetime_field
    actual_start_time: datetime = iso8601_datetime_field
    concurrent_viewers: int
    scheduled_end_time: datetime = iso8601_datetime_field
    scheduled_start_time: datetime = iso8601_datetime_field
