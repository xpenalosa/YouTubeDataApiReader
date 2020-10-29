from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from youtube_data_reader.models.common.published_item_snippet import PublishedItemSnippet


@dataclass_json
@dataclass
class LocalizedChannelInfo:
    description: str
    title: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelSnippet(PublishedItemSnippet):
    country: str
    custom_url: str
    default_language: str
    localized: LocalizedChannelInfo
