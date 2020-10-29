from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BrandingChannel:
    country: str
    default_language: str
    default_tab: str
    description: str
    featured_channels_title: str
    featured_channels_urls: List[str]
    keywords: str
    moderate_comments: bool
    profile_color: str
    show_browse_view: bool
    show_related_channels: bool
    title: str
    tracking_analytics_account_id: str
    unsubscribed_trailer: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BrandingWatch:
    background_color: str
    featured_playlist_id: str
    text_color: str


@dataclass_json
@dataclass
class ChannelBrandingSettings:
    channel: BrandingChannel
    watch: BrandingWatch
