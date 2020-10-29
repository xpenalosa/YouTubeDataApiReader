from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelStatus:
    is_linked: bool
    long_uploads_status: str
    made_for_kids: bool
    privacy_status: str
    self_declared_made_for_kids: bool
