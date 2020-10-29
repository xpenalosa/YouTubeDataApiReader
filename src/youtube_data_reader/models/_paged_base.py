from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class _PageInfo:
    results_per_page: int  # The number of results included in the API response.
    total_results: int  # The total number of results in the result set.


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class _PagedBase:
    """Base model for all API responses"""
    next_page_token: str  # Token that can be used as the pageToken parameter to get the next page in the result set.
    page_info: _PageInfo  # The pageInfo object encapsulates paging information for the result set.
