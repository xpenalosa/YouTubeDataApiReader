from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class ChannelContentOwnerDetails:
    content_owner: str
    time_linked: str  # FIXME: datetime
