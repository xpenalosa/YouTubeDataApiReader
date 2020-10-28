from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .model_base import ModelBase


@dataclass_json
@dataclass
class IdentifiedModelBase(ModelBase):
    id: str
