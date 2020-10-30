from typing import Dict

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.channel_sections.channel_section_content_details import ChannelSectionContentDetails
from youtube_data_reader.models.channel_sections.channel_section_targets import ChannelSectionTargets
from youtube_data_reader.models.common.localizations import LocalizationEntry
from youtube_data_reader.models.regions.region_snippet import RegionSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class ChannelSection(_IdentifiedModelBase):
    content_details: ChannelSectionContentDetails
    localizations: Dict[str, LocalizationEntry]
    snippet: RegionSnippet
    targeting: ChannelSectionTargets
