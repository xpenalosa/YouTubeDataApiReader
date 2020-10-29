from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PublishedSnippet:
    published_at: str  # FIXME: datetime
