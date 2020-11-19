from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoProcessingProgress:
    parts_processed: int
    parts_total: int
    time_left_ms: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoProcessingDetails:
    editor_suggestions_availability: str
    file_details_availability: str
    processing_failure_reason: str
    processing_issues_availability: str
    processing_progress: VideoProcessingProgress
    processing_status: str
    tag_suggestions_availability: str
    thumbnails_availability: str
