from youtube_data_reader.api.request_wrappers.captions_request_wrapper import get_captions

# This video ID is listed under the YouTube API documentation as an example for the captions endpoint
video_id = "M7FIvfx5J10"


def test_get_captions(api_key):
    response_body = get_captions(api_key, parts=["id"], video_id=video_id)
    assert response_body is not None
    assert response_body["kind"] == "youtube#captionListResponse"

    captions = response_body.get("items", None)  # type: list
    assert captions is not None
    assert len(captions) > 0

    first_caption = captions[0]  # type: dict
    assert first_caption["kind"] == "youtube#caption"
    assert first_caption["etag"] is not None
    assert first_caption["id"] is not None


def test_get_captions_snippet(api_key):
    response_body = get_captions(api_key, parts=["snippet"], video_id=video_id)
    first_caption = response_body.get("items", None)[0]  # type: dict

    snippet = first_caption["snippet"]  # type: dict
    assert snippet["videoId"] == video_id
    # 12 fields in the snippet structure for APIv3. See documentation for details.
    assert len(snippet) == 12
