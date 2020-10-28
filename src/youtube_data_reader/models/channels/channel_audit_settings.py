from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ChannelAuditDetails:
    communityGuidelinesGoodStanding: bool
    contentIdClaimsGoodStanding: bool
    copyrightStrikesGoodStanding: bool
    overallGoodStanding: bool
