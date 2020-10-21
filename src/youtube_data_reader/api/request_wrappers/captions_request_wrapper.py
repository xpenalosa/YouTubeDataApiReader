from typing import List

import requests

from youtube_data_reader.api.request_error_handler import RequestErrorHandler
from youtube_data_reader.api.request_handler import RequestHandler


class CaptionsRequestWrapper:

    @staticmethod
    @RequestErrorHandler.handle_http_errors
    def get_captions(key: str, parts: List[str], video_id: str, caption_ids: List[str] = None) -> requests.Response:
        """ Query the captions endpoint for the captions in a video.

        See https://developers.google.com/youtube/v3/docs/captions/list for complete documentation.

        :param key: Required API key.
        :param parts: Caption resource parts that the API response will include.
        :param video_id: The YouTube video ID of the video for which the API should return caption tracks.
        :param caption_ids: Each ID must identify a caption track associated with the specified video.
        :return: Response object associated with the request. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "videoId": video_id}
        if caption_ids:
            param_dict["id"] = ",".join(caption_ids)
        return RequestHandler.request("channels", param_dict)
