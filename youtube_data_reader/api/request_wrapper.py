import requests
from typing import List

from youtube_data_reader.api.request_error_handler import RequestErrorHandler
from youtube_data_reader.api.request_handler import RequestHandler


class RequestWrapper:

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_captions(key: str, parts: List[str], video_id: str, track_ids: List[str] = None) -> requests.Response:
        """ Query the captions endpoint.

        See https://developers.google.com/youtube/v3/docs/captions/list for complete documentation.

        :param key: Required API key.
        :param parts: Caption resource parts that the API response will include.
        :param video_id: The YouTube video ID of the video for which the API should return caption tracks.
        :param track_ids: Each ID must identify a caption track associated with the specified video.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "videoId": video_id}
        if track_ids:
            param_dict["id"] = ",".join(track_ids)
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_channels(key: str, parts: List[str], channel_ids: List[str], max_results: int = 5, page_token: str = None,
                     localization_code: str = None) -> requests.Response:
        """ Query the channels endpoint.

        See https://developers.google.com/youtube/v3/docs/channels/list for complete documentation.

        :param key: Required API key.
        :param parts: Channel resource properties that the API response will include.
        :param channel_ids: List of YouTube channel IDs for the resource(s) that are being retrieved.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "maxResults": max_results,
            "id": ",".join(channel_ids)}
        if page_token:
            param_dict["pageToken"] = page_token
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_user_channel(key: str, parts: List[str], username: str, max_results: int = 5, page_token: str = None,
                         localization_code: str = None) -> requests.Response:
        """ Query the channels endpoint.

        See https://developers.google.com/youtube/v3/docs/channels/list for complete documentation.

        :param key: Required API key.
        :param parts: Channel resource properties that the API response will include.
        :param username: Specifies a YouTube username, thereby requesting the channel associated with that username.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "maxResults": max_results,
            "forUsername": username}
        if page_token:
            param_dict["pageToken"] = page_token
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_channel_sections(key: str, parts: List[str], channel_ids: List[str] = None,
                             localization_code: str = None) -> requests.Response:
        """ Query the channel sections endpoint.

        See https://developers.google.com/youtube/v3/docs/channelSections/list for complete documentation.

        :param key: Required API key.
        :param parts: ChannelSection resource properties that the API response will include.
        :param channel_ids: IDs that uniquely identify the channelSection resources that are being retrieved.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(channel_ids)}
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_comments(key: str, parts: List[str], comment_ids: List[str],
                     text_format: str = "html") -> requests.Response:
        """ Query the comments endpoint.

        See https://developers.google.com/youtube/v3/docs/comments/list for complete documentation.

        :param key: Required API key.
        :param parts: Comment resource properties that the API response will include.
        :param comment_ids: Comment IDs for the resources that are being retrieved.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(comment_ids),
            "textFormat": text_format}
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_comment_responses(key: str, parts: List[str], comment_id: str, max_results: int = 20,
                              page_token: str = None, text_format: str = "html") -> requests.Response:
        """ Query the comments endpoint for the responses to a comment.

        See https://developers.google.com/youtube/v3/docs/comments/list for complete documentation.

        :param key: Required API key.
        :param parts: Comment resource properties that the API response will include.
        :param comment_id: ID of the comment for which replies should be retrieved.
        :param max_results: Maximum items that should be returned in the result set. Values between 1 to 100, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "parentId": comment_id,
            "maxResults": max_results,
            "textFormat": text_format}
        if page_token:
            param_dict["pageToken"] = page_token
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_comment_threads(key: str, parts: List[str], thread_ids: List[str], max_results: int = 20,
                            order: str = "time", page_token: str = None, search_terms: str = None,
                            text_format: str = "html") -> requests.Response:
        """ Query the comment threads endpoint.

        See https://developers.google.com/youtube/v3/docs/commentThreads/list for complete documentation.


        :param key: Required API key.
        :param parts: CommentThread resource properties that the API response will include.
        :param thread_ids: List of comment thread IDs.
        :param max_results: Maximum items that should be returned in the result set. Values between 1 to 100, inclusive.
        :param order: Whether the threads should be sorted by "time" or "relevance".
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param search_terms: Limit the API response to only contain comments that contain the specified search terms.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(thread_ids),
            "maxResults": max_results,
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_comment_threads_in_video(key: str, parts: List[str], video_id: str, max_results: int = 20,
                                     order: str = "time", page_token: str = None, search_terms: str = None,
                                     text_format: str = "html") -> requests.Response:
        """ Query the comment threads endpoint.

        See https://developers.google.com/youtube/v3/docs/commentThreads/list for complete documentation.


        :param key: Required API key.
        :param parts: CommentThread resource properties that the API response will include.
        :param video_id: The ID of the video to retrieve threads from.
        :param max_results: Maximum items that should be returned in the result set. Values between 1 to 100, inclusive.
        :param order: Whether the threads should be sorted by "time" or "relevance".
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param search_terms: Limit the API response to only contain comments that contain the specified search terms.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "videoId": video_id,
            "maxResults": max_results,
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_comment_threads_by_channel(key: str, parts: List[str], channel_id: str = None, max_results: int = 20,
                                       order: str = "time", page_token: str = None, search_terms: str = None,
                                       text_format: str = "html") -> requests.Response:
        """ Query the comment threads endpoint for threads that contain messages posted by a certain channel.

        See https://developers.google.com/youtube/v3/docs/commentThreads/list for complete documentation.

        :param key: Required API key.
        :param parts: CommentThread resource properties that the API response will include.
        :param channel_id: The ID of the channel to retrieve comment threads from.
        :param max_results: Maximum items that should be returned in the result set. Values between 1 to 100, inclusive.
        :param order: Whether the threads should be sorted by "time" or "relevance".
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param search_terms: Limit the API response to only contain comments that contain the specified search terms.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "channelId": channel_id,
            "maxResults": max_results,
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_comment_threads_related_to_channel(key: str, parts: List[str], channel_id: str = None,
                                               max_results: int = 20, order: str = "time", page_token: str = None,
                                               search_terms: str = None,
                                               text_format: str = "html") -> requests.Response:
        """ Query the comment threads endpoint for threads that contain messages posted by or in a certain channel.

        See https://developers.google.com/youtube/v3/docs/commentThreads/list for complete documentation.

        :param key: Required API key.
        :param parts: CommentThread resource properties that the API response will include.
        :param channel_id: The ID of the channel to retrieve comment threads from.
        :param max_results: Maximum items that should be returned in the result set. Values between 1 to 100, inclusive.
        :param order: Whether the threads should be sorted by "time" or "relevance".
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param search_terms: Limit the API response to only contain comments that contain the specified search terms.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "allThreadsRelatedToChannelId": channel_id,
            "maxResults": max_results,
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_languages(key: str, localization_code: str = None) -> requests.Response:
        """ Query the languages endpoint.

        See https://developers.google.com/youtube/v3/docs/i18nLanguages/list for complete documentation.

        :param key: Required API key.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": "snippet"
        }
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("i18nLanguages", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_regions(key: str, localization_code: str = None) -> requests.Response:
        """ Query the regions endpoint.

        See https://developers.google.com/youtube/v3/docs/i18nRegions/list for complete documentation.

        :param key: Required API key.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": "snippet"
        }
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("i18nRegions", param_dict)
