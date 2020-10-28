from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class BrandingChannel:
    country: str
    defaultLanguage: str
    defaultTab: str
    description: str
    featuredChannelsTitle: str
    featuredChannelsUrls: List[str]
    keywords: str
    moderateComments: bool
    profileColor: str
    showBrowseView: bool
    showRelatedChannels: bool
    title: str
    trackingAnalyticsAccountId: str
    unsubscribedTrailer: str


@dataclass_json
@dataclass
class BrandingWatch:
    backgroundColor: str
    featuredPlaylistId: str
    textColor: str


@dataclass_json
@dataclass
class ChannelBrandingSettings:
    channel: BrandingChannel
    watch: BrandingWatch
