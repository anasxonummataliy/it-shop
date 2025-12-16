import os
import asyncio

from aiogram import Bot, Dispatcher
from app.database.models import async_main
from dotenv import load_dotenv

from app.handlers import router

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())