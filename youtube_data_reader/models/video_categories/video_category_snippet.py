from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoCategorySnippet:
    assignable: bool
    channel_id: str = "UCBR8-60-B28hp2BmDPdntcQ"
    title: str
