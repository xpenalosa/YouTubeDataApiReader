from dataclasses_json import dataclass_json

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class LocalizationEntry:
    description: str
    title: str
