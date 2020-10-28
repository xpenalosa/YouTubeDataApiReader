from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RelatedPlaylists:
    likes: str
    favorites: str
    uploads: str


@dataclass_json
@dataclass
class ChannelContentDetails:
    relatedPlaylists: RelatedPlaylists
