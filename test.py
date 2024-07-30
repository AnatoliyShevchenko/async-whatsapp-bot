# Asyncio
import asyncio

# Local
from src.whatsapp import Whatsapp

NUMBER_ID = "number_id"
TOKEN = "your token"

async def main():
    bot = Whatsapp(number_id=NUMBER_ID, token=TOKEN)
    # temp = await bot.send_text_message(
    #     recipient_phone_number="number",
    #     text_message="Привет из питона!"
    # )
    temp = await bot.send_sample_text_message(
        recipient_phone_number="number",
        sample_name="agreement"
    )


if __name__ == "__main__":
    asyncio.run(main=main())
