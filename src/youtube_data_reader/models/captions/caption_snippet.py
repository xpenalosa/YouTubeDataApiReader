from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class CaptionSnippet:
    audioTrackType: str
    failureReason: str
    isAutoSynced: bool
    isCC: bool
    isDraft: bool
    isEasyReader: bool
    isLarge: bool
    language: str
    lastUpdated: str  # FIXME: datetime
    name: str
    status: str
    trackKind: str
    videoId: str
