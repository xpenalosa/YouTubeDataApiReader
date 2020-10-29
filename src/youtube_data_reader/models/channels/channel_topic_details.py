from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelTopicDetails:
    topic_categories: List[str]
    topic_ids: List[str]
