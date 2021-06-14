import logging
from os import environ

from aiogram import Bot, Dispatcher, executor

from krasivo_bot.config import Config
from krasivo_bot.handlers import inline_krasivo_text_handler


def main():
    logging.basicConfig(level=logging.INFO)
    config = Config(telegram_token=environ["TELEGRAM_TOKEN"])

    bot = Bot(token=config.telegram_token, parse_mode="HTML")
    dp = Dispatcher(bot)

    dp.register_inline_handler(inline_krasivo_text_handler)

    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
