from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.common.item_privacy_status import ItemPrivacyStatus
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class ChannelStatus(ItemPrivacyStatus):
    is_linked: bool
    long_uploads_status: str
    made_for_kids: bool
    self_declared_made_for_kids: bool
