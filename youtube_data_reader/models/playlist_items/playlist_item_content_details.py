from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass, iso8601_datetime_field


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class PlaylistItemContentDetails:
    end_at: str
    note: str
    start_at: str
    video_id: str
    video_published_at: datetime = iso8601_datetime_field()
