from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class SearchResultId:
    kind: str
    video_id: str
    channel_id: str
    playlist_id: str
