from typing import List

from dataclasses_json import dataclass_json

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.comment_threads.comment_thread_snippet import CommentThreadSnippet
from youtube_data_reader.models.comments.comment import Comment
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class CommentThreadReplies:
    comments: List[Comment]


@dataclass_json
@defaulted_dataclass
class CommentThread(_IdentifiedModelBase):
    snippet: CommentThreadSnippet
    replies: CommentThreadReplies
