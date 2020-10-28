from dataclasses import dataclass
from typing import Dict

from dataclasses_json import dataclass_json

from youtube_data_reader.models.channels.channel_audit_settings import ChannelAuditDetails
from youtube_data_reader.models.channels.channel_branding import ChannelBrandingSettings
from youtube_data_reader.models.channels.channel_content_details import ChannelContentDetails
from youtube_data_reader.models.channels.channel_content_owner_details import ChannelContentOwnerDetails
from youtube_data_reader.models.channels.channel_localizations import ChannelLocalizationEntry
from youtube_data_reader.models.channels.channel_snippet import ChannelSnippet
from youtube_data_reader.models.channels.channel_statistics import ChannelStatistics
from youtube_data_reader.models.channels.channel_status import ChannelStatus
from youtube_data_reader.models.channels.channel_topic_details import ChannelTopicDetails
from youtube_data_reader.models.identified_model_base import IdentifiedModelBase


@dataclass_json
@dataclass
class Channel(IdentifiedModelBase):
    auditDetails: ChannelAuditDetails
    brandingSettings: ChannelBrandingSettings
    contentDetails: ChannelContentDetails
    contentOwnerDetails: ChannelContentOwnerDetails
    localizations: Dict[str: ChannelLocalizationEntry]
    snippet: ChannelSnippet
    statistics: ChannelStatistics
    status: ChannelStatus
    topicDetails: ChannelTopicDetails
