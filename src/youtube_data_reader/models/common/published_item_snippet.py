from dataclasses import dataclass
from typing import Dict

from dataclasses_json import dataclass_json

from youtube_data_reader.models.common.published_snippet import PublishedSnippet


@dataclass_json
@dataclass
class ThumbnailItem:
    url: str
    width: int
    height: int


@dataclass_json
@dataclass
class PublishedItemSnippet(PublishedSnippet):
    description: str
    title: str
    thumbnails: Dict[str, ThumbnailItem]
