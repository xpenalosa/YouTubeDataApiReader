from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class ChannelAuditDetails:
    community_guidelines_good_standing: bool
    content_id_claims_good_standing: bool
    copyright_strikes_good_standing: bool
    overall_good_standing: bool
