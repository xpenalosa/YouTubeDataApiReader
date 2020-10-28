from dataclasses import dataclass

from dataclasses_json import dataclass_json

from youtube_data_reader.models.identified_model_base import IdentifiedModelBase
from youtube_data_reader.models.languages.language_snippet import LanguageSnippet


@dataclass_json
@dataclass
class Language(IdentifiedModelBase):
    snippet: LanguageSnippet
