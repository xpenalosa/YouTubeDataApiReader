from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ChannelStatus:
    privacyStatus: str
    isLinked: bool
    longUploadsStatus: str
    madeForKids: bool
    selfDeclaredMadeForKids: bool
