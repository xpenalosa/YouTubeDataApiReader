from typing import List

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
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
@defaulted_dataclass
class BrandingWatch:
    background_color: str
    featured_playlist_id: str
    text_color: str


@dataclass_json
@defaulted_dataclass
class ChannelBrandingSettings:
    channel: BrandingChannel
    watch: BrandingWatch
