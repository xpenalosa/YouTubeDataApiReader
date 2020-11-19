from typing import List

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.common.localizations import LocalizationEntry
from youtube_data_reader.models.common.published_item_snippet import PublishedItemSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoSnippet(PublishedItemSnippet):
    category_id: str
    channel_id: str
    channel_title: str
    default_audio_language: str
    default_language: str
    live_broadcast_content: str
    localized: LocalizationEntry
    tags: List[str]
