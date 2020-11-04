from typing import List

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class TagSuggestion:
    category_restricts: List[str]
    tag: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoSuggestions:
    editor_suggestions: List[str]
    processing_errors: List[str]
    processing_hints: List[str]
    processing_warnings: List[str]
    tag_suggestions: List[TagSuggestion]
