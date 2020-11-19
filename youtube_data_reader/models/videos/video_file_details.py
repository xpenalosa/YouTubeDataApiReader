from typing import List

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class MediaStream:
    codec: str
    bitrate_bps: int
    vendor: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoStream(MediaStream):
    aspect_ratio: float
    frame_rate_fps: float
    height_pixels: int
    rotation: str
    width_pixels: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class AudioStream(MediaStream):
    channel_count: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@defaulted_dataclass
class VideoFileDetails:
    audio_streams: List[AudioStream]
    bitrate_bps: int
    container: str
    creation_time: str
    duration_ms: int
    file_name: str
    file_size: int
    file_type: str
    video_streams: List[VideoStream]
