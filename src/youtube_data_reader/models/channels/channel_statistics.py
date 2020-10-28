from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ChannelStatistics:
    viewCount: int
    subscriberCount: int
    hiddenSubscriberCount: bool
    videoCount: int
