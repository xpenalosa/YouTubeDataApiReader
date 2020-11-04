from dataclasses import field
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase, config

from youtube_data_reader.models.utils import defaulted_dataclass, iso8601_datetime_field


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class CaptionSnippet:
    """Contains basic details about the caption."""
    audio_track_type: str
    failure_reason: str
    is_auto_synced: bool
    is_cc: bool = field(metadata=config(field_name="isCC"))
    is_draft: bool
    is_easy_reader: bool
    is_large: bool
    language: str
    last_updated: datetime = iso8601_datetime_field
    name: str
    status: str
    track_kind: str
    video_id: str
