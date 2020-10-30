from typing import Dict

from dataclasses_json import dataclass_json

from youtube_data_reader.models.common.published_snippet import PublishedSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class ThumbnailItem:
    height: int
    url: str
    width: int


@dataclass_json
@defaulted_dataclass
class PublishedItemSnippet(PublishedSnippet):
    description: str
    thumbnails: Dict[str, ThumbnailItem]
    title: str
