from dataclasses import field

from dataclasses_json import dataclass_json, LetterCase, config

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class CaptionSnippet:
    audio_track_type: str
    failure_reason: str
    is_auto_synced: bool
    is_cc: bool = field(metadata=config(field_name="isCC"))
    is_draft: bool
    is_easy_reader: bool
    is_large: bool
    language: str
    last_updated: str  # FIXME: datetime
    name: str
    status: str
    track_kind: str
    video_id: str
