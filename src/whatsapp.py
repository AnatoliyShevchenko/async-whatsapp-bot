# AioHTTP
from aiohttp import ClientResponse, ClientError

# Local
from .aio_requests import AioClient
from .logger import log
from .message import form_message, get_headers_from_token


class Whatsapp:

    def __init__(
        self, number_id: int, token: str, version_number: str = "v20.0"
    ) -> None:
        self.id = number_id
        self.token = token
        self.version_number = version_number
        self.client = AioClient()
        self.base_url = f"https://graph.facebook.com/{self.version_number}/{self.id}"
        self.msg_url = self.base_url + "/messages"
        self.media_url = self.base_url + "/media"

    async def send_text_message(
        self, recipient_phone_number: str, text_message: str
    ):
        data = form_message(
            phone_num=recipient_phone_number, text=text_message
        )
        headers = get_headers_from_token(wa_token=self.token)
        response_data = {}
        try:
            response: ClientResponse = \
                await self.client.make_post_request(
                    url=self.msg_url, headers=headers, data=data
                )
            response_data = await response.json()
            if response.status == 200:
                log.info(msg=f"Message id: {response_data["messages"][0]["id"]}")
            elif response.status == 401:
                log.error(msg="Cannot make request, "
                        "check your number_id or token!")
            else:
                log.error(
                    msg=f"Unknown error with code: {response.status}"
                )
        except ClientError as ce:
            log.error(msg="Client Error happend:", exc_info=ce)
        except Exception as e:
            log.error(msg="Unknown error:", exc_info=e)
        finally:
            await self.client.close_session()
            return response_data
