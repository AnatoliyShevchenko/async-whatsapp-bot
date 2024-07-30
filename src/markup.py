class Reply_markup:
    def __init__(self, markup) -> None:
        self.markup = markup


class Inline_button:
    def __init__(self, text: str, button_id: str = None):
        self.button = {
            "type": "reply",
            "reply": {
                "id": button_id if button_id else text,
                "title": text
            }
        }