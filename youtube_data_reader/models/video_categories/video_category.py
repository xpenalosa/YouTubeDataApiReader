from dataclasses_json import dataclass_json

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.utils import defaulted_dataclass
from youtube_data_reader.models.video_categories.video_category_snippet import VideoCategorySnippet


@dataclass_json()
@defaulted_dataclass
class VideoCategory(_IdentifiedModelBase):
    snippet: VideoCategorySnippet
