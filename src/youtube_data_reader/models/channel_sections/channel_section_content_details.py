from typing import List

from dataclasses_json import dataclass_json

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class ChannelSectionContentDetails(_IdentifiedModelBase):
    """Contains details about the section's content, such as a list of playlists or channels featured in the section."""
    channels: List[str]
    playlists: List[str]
