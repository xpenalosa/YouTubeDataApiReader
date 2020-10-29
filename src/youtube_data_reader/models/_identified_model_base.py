from dataclasses import dataclass
from dataclasses_json import dataclass_json

from youtube_data_reader.models._model_base import _ModelBase


@dataclass_json
@dataclass
class _IdentifiedModelBase(_ModelBase):
    id: str
