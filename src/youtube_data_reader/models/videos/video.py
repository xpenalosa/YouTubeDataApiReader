from typing import Dict

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.common.localizations import LocalizationEntry
from youtube_data_reader.models.utils import defaulted_dataclass
from youtube_data_reader.models.videos.video_content_details import VideoContentDetails
from youtube_data_reader.models.videos.video_file_details import VideoFileDetails
from youtube_data_reader.models.videos.video_live_streaming_details import VideoLiveStreamingDetails
from youtube_data_reader.models.videos.video_player import VideoPlayer
from youtube_data_reader.models.videos.video_processing_details import VideoProcessingDetails
from youtube_data_reader.models.videos.video_snippet import VideoSnippet
from youtube_data_reader.models.videos.video_statistics import VideoStatistics
from youtube_data_reader.models.videos.video_status import VideoStatus
from youtube_data_reader.models.videos.video_suggestions import VideoSuggestions
from youtube_data_reader.models.videos.video_topic_details import VideoTopicDetails


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class Video(_IdentifiedModelBase):
    content_details: VideoContentDetails
    file_details: VideoFileDetails
    live_streaming_details: VideoLiveStreamingDetails
    localizations: Dict[str, LocalizationEntry]
    player: VideoPlayer
    processing_details: VideoProcessingDetails
    recording_details: Dict[str, str]  # FIXME: datetime
    snippet: VideoSnippet
    statistics: VideoStatistics
    status: VideoStatus
    suggestions: VideoSuggestions
    topic_details: VideoTopicDetails
