from typing import List

from youtube_data_reader.api.request_handler import RequestHandler


def get_abuse_report_reasons(key: str, parts: List[str], localization_code: str = None) -> dict:
    """ Query the video abuse report reasons endpoint.

    See https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list for complete documentation.

    :param key: Required API key.
    :param parts: VideoAbuseReportReason resource properties that the API response will include.
    :param localization_code: BCP-47 code that uniquely identifies a language for localization.
    :return: JSON object associated with the query endpoint. See documentation for details.
    """
    param_dict = {
        "key": key,
        "part": ",".join(parts)
    }
    if localization_code:
        param_dict["hl"] = localization_code
    return RequestHandler.query_endpoint("videoAbuseReportReasons", param_dict)
