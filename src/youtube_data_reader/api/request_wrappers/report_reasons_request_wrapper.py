from typing import List

import requests

from youtube_data_reader.api.request_error_handler import RequestErrorHandler
from youtube_data_reader.api.request_handler import RequestHandler


class ReportReasonsRequestWrapper:

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_abuse_report_reasons(key: str, parts: List[str],  localization_code: str = None) -> requests.Response:
        """ Query the video abuse report reasons endpoint.

        See https://developers.google.com/youtube/v3/docs/i18nRegions/list for complete documentation.

        :param key: Required API key.
        :param parts: VideoAbuseReportReason resource properties that the API response will include.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts)
        }
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.request("videoAbuseReportReasons", param_dict)