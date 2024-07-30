# Asyncio
import asyncio

# Local
from src.whatsapp import Whatsapp

TOKEN = "token"

async def main():
    bot = Whatsapp(number_id="403231522866580", token=TOKEN)
    temp = await bot.send_text_message(
        recipient_phone_number="number",
        text_message="Привет из питона!"
    )
    breakpoint()


if __name__ == "__main__":
    asyncio.run(main=main())
