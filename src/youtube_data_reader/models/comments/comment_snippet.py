from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.common.published_item_snippet import PublishedItemSnippet


@dataclass_json
@dataclass
class CommentAuthorChannelId:
    value: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CommentSnippet(PublishedItemSnippet):
    author_channel_id: CommentAuthorChannelId
    author_channel_url: str
    author_display_name: str
    author_profile_image_url: str
    can_rate: bool
    channel_id: str
    like_count: int
    moderation_status: str
    parent_id: str
    text_display: str
    text_original: str
    updated_at: str  # FIXME: datetime
    video_id: str
    viewer_rating: str
