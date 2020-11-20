from typing import List

from youtube_data_reader.api.request_handler import query_endpoint


def get_videos(key: str, parts: List[str], video_ids: List[str], localization_code: str = None,
               max_height: int = None, max_width: int = None) -> dict:
    """ Query the videos endpoint.

    See https://developers.google.com/youtube/v3/docs/videos/list for complete documentation.

    :param key: Required API key.
    :param parts: ChannelSection resource properties that the API response will include.
    :param video_ids: IDs of the videos to retrieve.
    :param localization_code: BCP-47 code that uniquely identifies a language for localization.
    :param max_width: Maximum width of the embedded player returned in the player.embedHtml property. 72 to 8192.
    :param max_height: Maximum height of the embedded player returned in the player.embedHtml property. 72 to 8192.
    :return: JSON object associated with the query endpoint. See documentation for details.
    """
    param_dict = {
        "key": key,
        "part": ",".join(parts),
        "id": ",".join(video_ids)}
    if localization_code:
        param_dict["hl"] = localization_code
    if max_height:
        # Value 0 is invalid so truthy value check is enough
        param_dict["maxHeight"] = max(72, min(8192, max_height))
    if max_width:
        # Value 0 is invalid so truthy value check is enough
        param_dict["maxWidth"] = max(72, min(8192, max_width))
    return query_endpoint("videos", param_dict)


def get_popular_videos(key: str, parts: List[str], localization_code: str = None, max_results: int = 5,
                       max_height: int = None, max_width: int = None, page_token: str = None,
                       region_code: str = None, category_id: str = "0") -> dict:
    """ Query the videos endpoint for the most popular videos in a category and/or region.

    See https://developers.google.com/youtube/v3/docs/videos/list for complete documentation.

    :param key: Required API key.
    :param parts: ChannelSection resource properties that the API response will include.
    :param localization_code: BCP-47 code that uniquely identifies a language for localization.
    :param max_results: Maximum items that should be returned in the result set. Values between 1 to 50, inclusive.
    :param max_width: Maximum width of the embedded player returned in the player.embedHtml property. 72 to 8192.
    :param max_height: Maximum height of the embedded player returned in the player.embedHtml property. 72 to 8192.
    :param page_token: Identifies a specific page in the result set that should be returned.
    :param category_id: Video category for which the popular videos should be retrieved.
    :param region_code: ISO 3166-1 alpha-2 code for the country to retrieve popular videos from.
    :return: JSON object associated with the query endpoint. See documentation for details.
    """
    param_dict = {
        "key": key,
        "part": ",".join(parts),
        "chart": "mostPopular",
        "maxResults": max(1, min(50, max_results)),
        "videoCategoryId": category_id}
    if localization_code:
        param_dict["hl"] = localization_code
    if max_height:
        # Value 0 is invalid so truthy value check is enough
        param_dict["maxHeight"] = max(72, min(8192, max_height))
    if max_width:
        # Value 0 is invalid so truthy value check is enough
        param_dict["maxWidth"] = max(72, min(8192, max_width))
    if page_token:
        param_dict["pageToken"] = page_token
    if region_code:
        param_dict["regionCode"] = region_code

    return query_endpoint("videos", param_dict)
