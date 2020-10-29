from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelContentOwnerDetails:
    content_owner: str
    time_linked: str  # FIXME: datetime
