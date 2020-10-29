from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.playlist_items.playlist_item_snippet import PlaylistItemSnippet


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlaylistItem(_IdentifiedModelBase):
    snippet: PlaylistItemSnippet
    content_details: str
    status: str
