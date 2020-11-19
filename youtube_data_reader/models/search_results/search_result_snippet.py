from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.common.published_item_snippet import PublishedItemSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class SearchResultSnippet(PublishedItemSnippet):
    channel_id: str
    channel_title: str
    live_broadcast_content: str
