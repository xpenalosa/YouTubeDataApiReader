from typing import List

from youtube_data_reader.api.request_handler import RequestHandler


def get_channels(key: str, parts: List[str], channel_ids: List[str], max_results: int = 5, page_token: str = None,
                 localization_code: str = None) -> dict:
    """ Query the channels endpoint.

    See https://developers.google.com/youtube/v3/docs/channels/list for complete documentation.

    :param key: Required API key.
    :param parts: Channel resource properties that the API response will include.
    :param channel_ids: List of YouTube channel IDs for the resource(s) that are being retrieved.
    :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
    :param page_token: Identifies a specific page in the result set that should be returned.
    :param localization_code: BCP-47 code that uniquely identifies a language for localization.
    :return: JSON object associated with the query endpoint. See documentation for details.
    """
    param_dict = {
        "key": key,
        "part": ",".join(parts),
        "maxResults": max(0, min(50, max_results)),
        "id": ",".join(channel_ids)}
    if page_token:
        param_dict["pageToken"] = page_token
    if localization_code:
        param_dict["hl"] = localization_code
    return RequestHandler.query_endpoint("channels", param_dict)


def get_user_channel(key: str, parts: List[str], username: str, max_results: int = 5, page_token: str = None,
                     localization_code: str = None) -> dict:
    """ Query the channels endpoint for a channel with a specific username.

    See https://developers.google.com/youtube/v3/docs/channels/list for complete documentation.

    :param key: Required API key.
    :param parts: Channel resource properties that the API response will include.
    :param username: Specifies a YouTube username, thereby requesting the channel associated with that username.
    :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
    :param page_token: Identifies a specific page in the result set that should be returned.
    :param localization_code: BCP-47 code that uniquely identifies a language for localization.
    :return: JSON object associated with the query endpoint. See documentation for details.
    """
    param_dict = {
        "key": key,
        "part": ",".join(parts),
        "maxResults": max(0, min(50, max_results)),
        "forUsername": username}
    if page_token:
        param_dict["pageToken"] = page_token
    if localization_code:
        param_dict["hl"] = localization_code
    return RequestHandler.query_endpoint("channels", param_dict)
