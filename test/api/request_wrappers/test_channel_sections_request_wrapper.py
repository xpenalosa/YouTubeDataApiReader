from youtube_data_reader.api.request_wrappers.channel_sections_request_wrapper import get_channel_sections, \
    get_channel_sections_by_id

# This channel ID is listed under the YouTube API documentation as an example for the channel sections endpoint
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
channel_section_ids = ["UC_x5XG1OV2P6uZZ5FSM9Ttw.jNQXAC9IVRw", "UC_x5XG1OV2P6uZZ5FSM9Ttw.ebKlgRwnpFY"]


def test_get_channel_sections(api_key):
    response_body = get_channel_sections(api_key, parts=["id"], channel_id=channel_id)
    assert response_body["kind"] == "youtube#channelSectionListResponse"

    channel_sections = response_body.get("items", None)  # type: list
    assert len(channel_sections) > 0

    first_section = channel_sections[0]  # type: dict
    assert first_section["kind"] == "youtube#channelSection"


def test_get_channel_sections_parts(api_key, parts_validator):
    parts = ["contentDetails", "id", "localizations", "snippet"]
    response_body = get_channel_sections(api_key, parts=parts, channel_id=channel_id)
    # "contentDetails" and "localizations" are optional in the response, and depend on the type of channel section
    assert parts_validator(response_body, ["id", "snippet"])

    first_item = response_body.get("items", None)[0]  # type: dict
    assert first_item["snippet"]["channelId"] == channel_id


def test_get_channel_sections_by_id(api_key):
    response_body = get_channel_sections_by_id(api_key, parts=["id"], channel_section_ids=channel_section_ids)
    assert response_body["kind"] == "youtube#channelSectionListResponse"

    channel_sections = response_body.get("items", None)  # type: list
    assert len(channel_sections) == len(channel_section_ids)

    first_section = channel_sections[0]  # type: dict
    assert first_section["kind"] == "youtube#channelSection"
    assert first_section["id"] in channel_section_ids


def test_get_channel_sections_by_id_parts(api_key, parts_validator):
    parts = ["contentDetails", "id", "localizations", "snippet"]
    response_body = get_channel_sections_by_id(api_key, parts=parts, channel_section_ids=channel_section_ids)
    # "contentDetails" and "localizations" are optional in the response, and depend on the type of channel section
    assert parts_validator(response_body, ["id", "snippet"])

    channel_sections = response_body["items"]  # type: list
    assert len(channel_sections) == len(channel_section_ids)

    assert channel_sections[0]["snippet"]["channelId"] == channel_id
