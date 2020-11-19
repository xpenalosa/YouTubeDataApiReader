from typing import List

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoTopicDetails:
    relevant_topic_ids: List[str]
    topic_categories: List[str]
    topic_ids: List[str]
