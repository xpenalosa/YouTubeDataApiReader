from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.common.item_privacy_status import ItemPrivacyStatus
from youtube_data_reader.models.playlist_items.playlist_item_content_details import PlaylistItemContentDetails
from youtube_data_reader.models.playlist_items.playlist_item_snippet import PlaylistItemSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class PlaylistItem(_IdentifiedModelBase):
    content_details: PlaylistItemContentDetails
    snippet: PlaylistItemSnippet
    status: ItemPrivacyStatus
