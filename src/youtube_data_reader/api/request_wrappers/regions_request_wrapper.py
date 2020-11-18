from youtube_data_reader.api.request_handler import RequestHandler


def get_regions(key: str, localization_code: str = None) -> dict:
    """ Query the regions endpoint.

    See https://developers.google.com/youtube/v3/docs/i18nRegions/list for complete documentation.

    :param key: Required API key.
    :param localization_code: BCP-47 code that uniquely identifies a language for localization.
    :return: JSON object associated with the query endpoint. See documentation for details.
    """
    param_dict = {
        "key": key,
        "part": "snippet"
    }
    if localization_code:
        param_dict["hl"] = localization_code
    return RequestHandler.query_endpoint("i18nRegions", param_dict)
