import hashlib
from textwrap import shorten

from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from krasivo_bot.transform import transform


async def inline_krasivo_text_handler(inline_query: InlineQuery):
    text = inline_query.query
    if not text:
        return

    transformed = transform(text)
    preview = shorten(transformed, 64)
    result_id = hashlib.md5(text.encode()).hexdigest()
    result_article = InlineQueryResultArticle(
        id=result_id,
        title=preview,
        input_message_content=InputTextMessageContent(transformed),
    )

    await inline_query.answer(results=[result_article])
