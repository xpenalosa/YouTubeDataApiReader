from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class RelatedPlaylists:
    likes: str
    favorites: str
    uploads: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class ChannelContentDetails:
    related_playlists: RelatedPlaylists
