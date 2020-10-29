from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, LetterCase, config


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
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
