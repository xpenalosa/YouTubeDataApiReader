from typing import List

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class SecondaryReportReason:
    id: str
    label: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class ReportReasonSnippet:
    label: str
    secondary_reasons: List[SecondaryReportReason]
