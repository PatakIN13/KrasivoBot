import re
from functools import partial
from typing import Callable

import bleach
from aiogram.utils import markdown

_PATTERN_TO_TRANSFORM = re.compile(r"{(?P<escop>{)?(?P<content>[^}]+)}")


def krasivo_transformer(text: str) -> str:
    krasivo_text = " ".join([ch.upper() for ch in text if ch.isalnum()])
    return markdown.hcode(krasivo_text)


def ladder_transformer(text: str) -> str:
    return "".join(ch.upper() if idx % 2 == 0 else ch.lower() for idx, ch in enumerate(text))


registered_transformers = {
    "𝓚𝓹𝓪𝓬𝓾𝓫𝓸": krasivo_transformer,
    "lAdDeR cAsE": ladder_transformer,
}


def _transform_part(match, transformer):
    if match["escop"]:
        return match.group(0)
    return transformer(match["content"])


def transform(text, transformer: Callable[[str], str] = krasivo_transformer) -> str:
    clean_text = bleach.clean(text, strip=True)
    if _PATTERN_TO_TRANSFORM.search(clean_text):
        return _PATTERN_TO_TRANSFORM.sub(partial(_transform_part, transformer=transformer), clean_text)
    return transformer(clean_text)
