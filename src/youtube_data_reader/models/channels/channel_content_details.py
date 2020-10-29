from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json
@dataclass
class RelatedPlaylists:
    likes: str
    favorites: str
    uploads: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelContentDetails:
    related_playlists: RelatedPlaylists
