import requests
from typing import Optional


def send_message(
    endpoint_url: str,
    text: str,
    image_url: Optional[str] = None,
):
    """Send a message to a mattermost channel

    Args:
        endpoint_url (str): URL of the mattermost endpoint (for bot)
        text (str): Text to send to a channel
        image_url (Optional[str], optional): Url of an image to link
        with your text. Defaults to None.
    """
    data = {}
    data["text"] = text
    if image_url:
        data["attachments"] = [{"image_url": image_url}]

    r = requests.post(endpoint_url, json=data)
    assert r.status_code == 200
