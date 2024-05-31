import logging
import asyncio

from aiogram import Bot, Dispatcher

from krasivo_bot.config import config
from krasivo_bot.handlers import router


def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    bot = Bot(token=config.telegram_token)

    dp.include_router(router)

    dp.run_polling(bot)


if __name__ == "__main__":
    main()
