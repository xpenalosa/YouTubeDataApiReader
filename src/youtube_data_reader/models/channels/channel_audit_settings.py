from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelAuditDetails:
    community_guidelines_good_standing: bool
    content_id_claims_good_standing: bool
    copyright_strikes_good_standing: bool
    overall_good_standing: bool
