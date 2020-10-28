from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PageInfo:
    resultsPerPage: int  # The number of results included in the API response.
    totalResults: int  # The total number of results in the result set.


@dataclass_json
@dataclass
class PagedBase:
    """Base model for all API responses"""
    nextPageToken: str  # Token that can be used as the pageToken parameter to retrieve the next page in the result set.
    pageInfo: PageInfo  # The pageInfo object encapsulates paging information for the result set.
