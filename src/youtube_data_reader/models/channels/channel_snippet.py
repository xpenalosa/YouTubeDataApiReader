from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ThumbnailItem:
    url: str
    width: int
    height: int


@dataclass_json
@dataclass
class Thumbnails:
    default: ThumbnailItem
    medium: ThumbnailItem
    high: ThumbnailItem


@dataclass_json
@dataclass
class LocalizedChannelInfo:
    title: str
    description: str


@dataclass_json
@dataclass
class ChannelSnippet:
    title: str
    description: str
    customUrl: str
    publishedAt: str  # FIXME: datetime
    thumbnails: Thumbnails
    defaultLanguage: str
    localized: LocalizedChannelInfo
    country: str
