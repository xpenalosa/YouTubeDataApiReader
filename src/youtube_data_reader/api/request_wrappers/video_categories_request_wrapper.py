from typing import List

import requests

from youtube_data_reader.api.request_error_handler import RequestErrorHandler
from youtube_data_reader.api.request_handler import RequestHandler


class VideoCategoriesRequestWrapper:

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_video_categories(key: str, category_ids: List[str], localization_code: str = None) -> requests.Response:
        """ Query the video categories endpoint.

        See https://developers.google.com/youtube/v3/docs/videoCategories/list for complete documentation.

        :param key: Required API key.
        :param category_ids: IDs for the resources that you are retrieving.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": "snippet",
            "id": ",".join(category_ids)}
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("videoCategories", param_dict)

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_video_categories_in_region(key: str, region_code: str, localization_code: str = None) -> requests.Response:
        """ Query the video categories endpoint for video categories in a specific region.

        See https://developers.google.com/youtube/v3/docs/videoCategories/list for complete documentation.

        :param key: Required API key.
        :param region_code: ISO 3166-1 alpha-2 code for the country to retrieve categories from.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": "snippet",
            "regionCode": region_code}
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("videoCategories", param_dict)
