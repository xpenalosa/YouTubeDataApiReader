from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.comments.comment import Comment
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class CommentThreadSnippet:
    channel_id: str
    video_id: str
    top_level_comment: Comment
    can_reply: bool
    total_reply_count: int
    is_public: bool
