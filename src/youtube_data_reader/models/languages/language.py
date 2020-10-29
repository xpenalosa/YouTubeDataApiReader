from dataclasses import dataclass

from dataclasses_json import dataclass_json

from youtube_data_reader.models._identified_model_base import _IdentifiedModelBase
from youtube_data_reader.models.languages.language_snippet import LanguageSnippet


@dataclass_json
@dataclass
class Language(_IdentifiedModelBase):
    snippet: LanguageSnippet
