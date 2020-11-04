from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoStatus:
    embeddable: bool
    failure_reason: str
    license: str
    made_for_kids: bool
    privacy_status: str
    public_stats_viewable: bool
    publish_at: str
    rejection_reason: str
    self_declared_made_for_kids: bool
    upload_status: str
