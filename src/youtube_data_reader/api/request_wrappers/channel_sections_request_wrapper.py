from typing import List

import requests

from youtube_data_reader.api.request_error_handler import RequestErrorHandler
from youtube_data_reader.api.request_handler import RequestHandler


class ChannelSectionsRequestWrapper:

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_channel_sections(key: str, parts: List[str], channel_id: str,
                             localization_code: str = None) -> requests.Response:
        """ Query the channel sections endpoint for a specific channel.

        See https://developers.google.com/youtube/v3/docs/channelSections/list for complete documentation.

        :param key: Required API key.
        :param parts: ChannelSection resource properties that the API response will include.
        :param channel_id: IDs of the channel to retrieve the sections from.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "channelId": ",".join(channel_id)}
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("channels", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_channel_sections_by_id(key: str, parts: List[str], channel_section_ids: List[str],
                                   localization_code: str = None) -> requests.Response:
        """ Query the channel sections endpoint.

        See https://developers.google.com/youtube/v3/docs/channelSections/list for complete documentation.

        :param key: Required API key.
        :param parts: ChannelSection resource properties that the API response will include.
        :param channel_section_ids: IDs that uniquely identify the channelSection resources that are being retrieved.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(channel_section_ids)}
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("channels", param_dict)
