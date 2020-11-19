from typing import Dict

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.common.published_item_snippet import ThumbnailItem
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class SubscriptionSubscriberSnippet:
    channel_id: str
    description: str
    thumbnails: Dict[str, ThumbnailItem]
    title: str
