from typing import Dict

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.common.item_privacy_status import ItemPrivacyStatus
from youtube_data_reader.models.common.localizations import LocalizationEntry
from youtube_data_reader.models.playlist_items.playlist_content_details import PlaylistContentDetails
from youtube_data_reader.models.playlist_items.playlist_player import PlaylistPlayer
from youtube_data_reader.models.playlists.playlist_snippet import PlaylistSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class Playlist(_IdentifiedModelBase):
    content_details: PlaylistContentDetails
    localizations: Dict[str: LocalizationEntry]
    player: PlaylistPlayer
    snippet: PlaylistSnippet
    status: ItemPrivacyStatus
