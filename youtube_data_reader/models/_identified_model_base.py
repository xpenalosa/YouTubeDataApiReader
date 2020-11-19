from dataclasses_json import dataclass_json

from youtube_data_reader.models._model_base import _ModelBase
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class _IdentifiedModelBase(_ModelBase):
    id: str
