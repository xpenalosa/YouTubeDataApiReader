from dataclasses_json import dataclass_json

from youtube_data_reader.models._model_base import _ModelBase
from youtube_data_reader.models.search_results.search_result_id import SearchResultId
from youtube_data_reader.models.search_results.search_result_snippet import SearchResultSnippet
from youtube_data_reader.models.utils import defaulted_dataclass


@dataclass_json
@defaulted_dataclass
class SearchResult(_ModelBase):
    id: SearchResultId
    snippet: SearchResultSnippet
