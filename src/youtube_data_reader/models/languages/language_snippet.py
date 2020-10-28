from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class LanguageSnippet:
    """Dataclass for the Language 'snippet' part"""
    hl: str  # BCP-47 code that uniquely identifies a language.
    name: str  # The name of the language as it is written in the language specified by LanguageSnippet.hl
