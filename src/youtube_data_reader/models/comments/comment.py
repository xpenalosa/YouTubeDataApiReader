from dataclasses import dataclass

from dataclasses_json import dataclass_json

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.comments.comment_snippet import CommentSnippet


@dataclass_json
@dataclass
class Comment(_IdentifiedModelBase):
    snippet: CommentSnippet
