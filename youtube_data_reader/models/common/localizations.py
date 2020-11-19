from dataclasses_json import dataclass_json

from youtube_data_reader.models.common.title_wrapper import TitleFieldWrapper
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class LocalizationEntry(TitleFieldWrapper):
    description: str
