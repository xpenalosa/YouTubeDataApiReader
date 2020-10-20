from typing import List

import requests

from youtube_data_reader.api.request_error_handler import RequestErrorHandler
from youtube_data_reader.api.request_handler import RequestHandler


class SubscriptionsRequestWrapper:

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_channel_subscriptions(key: str, parts: List[str], channel_id: str, to_channel_ids: List[str] = None,
                                  max_results: int = 5, order: str = "relevance",
                                  page_token: str = None) -> requests.Response:
        """ Query the subscriptions endpoint.

        See https://developers.google.com/youtube/v3/docs/subscriptions/list for complete documentation.

        :param key: Required API key.
        :param parts: PlaylistItem resource properties that the API response will include.
        :param channel_id: ID of the channel to retrieve subscriptions from.
        :param to_channel_ids: IDs of the subscribed channels. Acts as a filter.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param order: Whether the subscriptions should be sorted by "alphabetical", "relevance", or "unread".
        :param page_token: Identifies a specific page in the result set that should be returned.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "channelId": channel_id,
            "maxResults": max_results,
            "order": order}
        if to_channel_ids:
            param_dict["forChannelIds"] = ",".join(to_channel_ids)
        if page_token:
            param_dict["pageToken"] = page_token
        return RequestHandler.request("subscriptions", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_subscriptions(key: str, parts: List[str], subscription_ids: List[str], to_channel_ids: List[str] = None,
                          max_results: int = 5, order: str = "relevance", page_token: str = None) -> requests.Response:
        """ Query the subscriptions endpoint.

        See https://developers.google.com/youtube/v3/docs/subscriptions/list for complete documentation.

        :param key: Required API key.
        :param parts: PlaylistItem resource properties that the API response will include.
        :param subscription_ids: IDs of the subscriptions to retrieve.
        :param to_channel_ids: IDs of the subscribed channels. Acts as a filter.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param order: Whether the subscriptions should be sorted by "alphabetical", "relevance", or "unread".
        :param page_token: Identifies a specific page in the result set that should be returned.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(subscription_ids),
            "maxResults": max_results,
            "order": order}
        if to_channel_ids:
            param_dict["forChannelIds"] = ",".join(to_channel_ids)
        if page_token:
            param_dict["pageToken"] = page_token
        return RequestHandler.request("subscriptions", param_dict)