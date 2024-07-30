# Python
import json


def get_headers_from_token(wa_token: str) -> dict:
    return {
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {wa_token}"
    }

def form_message(
    phone_num: str, text: str, web_page_preview=False
) -> str:
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": phone_num,
        "type": "text",
        "text": {
            "preview_url": web_page_preview,
            "body": text
        }
    }
    return json.dumps(obj=data)
