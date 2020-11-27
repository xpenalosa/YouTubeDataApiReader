from youtube_data_reader.api.request_wrappers.captions_request_wrapper import get_captions

# This video ID is listed under the YouTube API documentation as an example for the captions endpoint
video_id = "M7FIvfx5J10"


def test_get_captions(api_key):
    response_body = get_captions(api_key, parts=["id"], video_id=video_id)
    assert response_body is not None
    assert response_body["kind"] == "youtube#captionListResponse"

    captions = response_body.get("items", None)  # type: list
    assert len(captions) > 0

    first_caption = captions[0]  # type: dict
    assert first_caption["kind"] == "youtube#caption"
    assert first_caption["etag"] is not None


def test_get_captions_parts(api_key, parts_validator):
    parts = ["id", "snippet"]
    response_body = get_captions(api_key, parts=parts, video_id=video_id)
    assert parts_validator(response_body, parts)

    first_item = response_body.get("items", None)[0]  # type: dict
    snippet = first_item["snippet"]  # type: dict
    assert snippet["videoId"] == video_id
    # 12 fields in the snippet structure for APIv3. See documentation for details.
    assert len(snippet) == 12


def test_get_captions_filtered(api_key):
    # ID for the french language captions in the video
    caption_id = "8yMV7mc691ZSpFoIXHN_HCCThRPxz_If"

    response_body = get_captions(api_key, parts=["id", "snippet"], video_id=video_id, caption_ids=[caption_id])
    captions = response_body["items"]  # type: list
    assert len(captions) == 1  # Only the requested captions are returned

    first_caption = captions[0]  # type: dict
    assert first_caption["kind"] == "youtube#caption"
    assert first_caption["id"] == caption_id
    assert first_caption["snippet"]["language"] == "fr"
