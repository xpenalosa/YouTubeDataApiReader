from dataclasses_json import dataclass_json

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.comments.comment_snippet import CommentSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class Comment(_IdentifiedModelBase):
    snippet: CommentSnippet
