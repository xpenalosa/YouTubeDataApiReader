from dataclasses import dataclass

from dataclasses_json import dataclass_json

from youtube_data_reader.models.captions.caption_snippet import CaptionSnippet
from youtube_data_reader.models.identified_model_base import IdentifiedModelBase


@dataclass_json
@dataclass
class Caption(IdentifiedModelBase):
    snippet: CaptionSnippet
