from typing import List

from youtube_data_reader.api.request_handler import RequestHandler


class CommentsRequestWrapper:
    """Request wrapper for the Comments and CommentThread endpoints."""

    @staticmethod
    def get_comments(key: str, parts: List[str], comment_ids: List[str], text_format: str = "html") -> dict:
        """ Query the comments endpoint.

        See https://developers.google.com/youtube/v3/docs/comments/list for complete documentation.

        :param key: Required API key.
        :param parts: Comment resource properties that the API response will include.
        :param comment_ids: Comment IDs for the resources that are being retrieved.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: Response object associated with the query_endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(comment_ids),
            "textFormat": text_format}
        return RequestHandler.query_endpoint("channels", param_dict)

    @staticmethod
    def get_comment_responses(key: str, parts: List[str], comment_id: str, max_results: int = 20,
                              page_token: str = None, text_format: str = "html") -> dict:
        """ Query the comments endpoint for the responses to a comment.

        See https://developers.google.com/youtube/v3/docs/comments/list for complete documentation.

        :param key: Required API key.
        :param parts: Comment resource properties that the API response will include.
        :param comment_id: ID of the comment for which replies should be retrieved.
        :param max_results: Maximum items that should be returned in the result set. Values between 1 to 100, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "parentId": comment_id,
            "maxResults": max(1, min(100, max_results)),
            "textFormat": text_format}
        if page_token:
            param_dict["pageToken"] = page_token
        return RequestHandler.query_endpoint("channels", param_dict)

    @staticmethod
    def get_comment_threads(key: str, parts: List[str], thread_ids: List[str], max_results: int = 20,
                            order: str = "time", page_token: str = None, search_terms: str = None,
                            text_format: str = "html") -> dict:
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
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(thread_ids),
            "maxResults": max(1, min(100, max_results)),
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.query_endpoint("channels", param_dict)

    @staticmethod
    def get_comment_threads_in_video(key: str, parts: List[str], video_id: str, max_results: int = 20,
                                     order: str = "time", page_token: str = None, search_terms: str = None,
                                     text_format: str = "html") -> dict:
        """ Query the comment threads endpoint for comment threads in a specific video.

        See https://developers.google.com/youtube/v3/docs/commentThreads/list for complete documentation.

        :param key: Required API key.
        :param parts: CommentThread resource properties that the API response will include.
        :param video_id: The ID of the video to retrieve threads from.
        :param max_results: Maximum items that should be returned in the result set. Values between 1 to 100, inclusive.
        :param order: Whether the threads should be sorted by "time" or "relevance".
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param search_terms: Limit the API response to only contain comments that contain the specified search terms.
        :param text_format: Indicates whether the API should return comments formatted as "html" or as "plainText".
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "videoId": video_id,
            "maxResults": max(1, min(100, max_results)),
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.query_endpoint("channels", param_dict)

    @staticmethod
    def get_comment_threads_by_channel(key: str, parts: List[str], channel_id: str = None, max_results: int = 20,
                                       order: str = "time", page_token: str = None, search_terms: str = None,
                                       text_format: str = "html") -> dict:
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
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "channelId": channel_id,
            "maxResults": max(1, min(100, max_results)),
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.query_endpoint("channels", param_dict)

    @staticmethod
    def get_comment_threads_related_to_channel(key: str, parts: List[str], channel_id: str = None,
                                               max_results: int = 20, order: str = "time", page_token: str = None,
                                               search_terms: str = None, text_format: str = "html") -> dict:
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
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "allThreadsRelatedToChannelId": channel_id,
            "maxResults": max(1, min(100, max_results)),
            "textFormat": text_format,
            "order": order}
        if page_token:
            param_dict["pageToken"] = page_token
        if search_terms:
            param_dict["searchTerms"] = search_terms
        return RequestHandler.query_endpoint("channels", param_dict)
