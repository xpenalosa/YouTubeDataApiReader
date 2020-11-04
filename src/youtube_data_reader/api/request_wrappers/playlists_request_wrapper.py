from typing import List

from youtube_data_reader.api.request_handler import RequestHandler


class PlaylistRequestWrapper:
    """Request wrapper for the Playlists and PlaylistItems endpoints."""

    @staticmethod
    def get_playlist_items(key: str, parts: List[str], playlist_id: str, max_results: int = 5, page_token: str = None,
                           video_id: str = None) -> dict:
        """ Query the playlist items endpoint for items in a specific playlist.

        See https://developers.google.com/youtube/v3/docs/playlistItems/list for complete documentation.

        :param key: Required API key.
        :param parts: PlaylistItem resource properties that the API response will include.
        :param playlist_id: ID of the playlist for which to retrieve playlist items.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param video_id: Specifies that the query should return only the items that contain the specified video.
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "playlistId": ",".join(playlist_id),
            "maxResults": max(0, min(50, max_results))}
        if page_token:
            param_dict["pageToken"] = page_token
        if video_id:
            param_dict["videoId"] = video_id
        return RequestHandler.query_endpoint("playlistItems", param_dict)

    @staticmethod
    def get_playlist_items_by_id(key: str, parts: List[str], playlist_item_ids: List[str], max_results: int = 5,
                                 page_token: str = None, video_id: str = None) -> dict:
        """ Query the playlist items endpoint.

        See https://developers.google.com/youtube/v3/docs/playlistItems/list for complete documentation.

        :param key: Required API key.
        :param parts: PlaylistItem resource properties that the API response will include.
        :param playlist_item_ids: IDs of the playlist items to retrieve.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param video_id: Specifies that the query should return only the items that contain the specified video.
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(playlist_item_ids),
            "maxResults": max(0, min(50, max_results))}
        if page_token:
            param_dict["pageToken"] = page_token
        if video_id:
            param_dict["videoId"] = video_id
        return RequestHandler.query_endpoint("playlistItems", param_dict)

    @staticmethod
    def get_channel_playlists(key: str, parts: List[str], channel_id: str, max_results: int = 5, page_token: str = None,
                              localization_code: str = None) -> dict:
        """ Query the playlists endpoint for playlists in a specific channel.

        See https://developers.google.com/youtube/v3/docs/playlists/list for complete documentation.

        :param key: Required API key.
        :param parts: PlaylistItem resource properties that the API response will include.
        :param channel_id: ID of the channel to retrieve playlists from.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "channelId": channel_id,
            "maxResults": max(0, min(50, max_results))}
        if page_token:
            param_dict["pageToken"] = page_token
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.query_endpoint("playlists", param_dict)

    @staticmethod
    def get_playlists(key: str, parts: List[str], playlist_ids: List[str], max_results: int = 5, page_token: str = None,
                      localization_code: str = None) -> dict:
        """ Query the playlists endpoint.

        See https://developers.google.com/youtube/v3/docs/playlists/list for complete documentation.

        :param key: Required API key.
        :param parts: PlaylistItem resource properties that the API response will include.
        :param playlist_ids: IDs of the playlists to retrieve.
        :param max_results: Maximum items that should be returned in the result set. Values between 0 to 50, inclusive.
        :param page_token: Identifies a specific page in the result set that should be returned.
        :param localization_code: BCP-47 code that uniquely identifies a language for localization.
        :return: JSON object associated with the query endpoint. See documentation for details.
        """
        param_dict = {
            "key": key,
            "part": ",".join(parts),
            "id": ",".join(playlist_ids),
            "maxResults": max(0, min(50, max_results))}
        if page_token:
            param_dict["pageToken"] = page_token
        if localization_code:
            param_dict["hl"] = localization_code
        return RequestHandler.query_endpoint("playlists", param_dict)
