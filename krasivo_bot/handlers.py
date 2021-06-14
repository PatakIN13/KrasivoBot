import hashlib
from textwrap import shorten

from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from krasivo_bot.transform import registered_transformers, transform


async def inline_krasivo_text_handler(inline_query: InlineQuery):
    text = inline_query.query
    if not text:
        return

    results = []
    for transformer_name, transformer in registered_transformers.items():
        transformed = transform(text, transformer)
        preview = shorten(transformed, 64)
        result_id = hashlib.md5(f"{transformer_name}_{text}".encode()).hexdigest()
        result_article = InlineQueryResultArticle(
            id=result_id,
            title=preview,
            input_message_content=InputTextMessageContent(transformed),
        )
        results.append(result_article)

    await inline_query.answer(results=results)
