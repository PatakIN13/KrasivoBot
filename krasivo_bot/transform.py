import re
from functools import partial
from typing import Callable, NamedTuple, Pattern

import bleach
from aiogram.utils import markdown


class Transformer(NamedTuple):
    name: str
    regex: Pattern  # should always contain the "content" group, which will be transformed
    transform: Callable[[str], str]


krasivo_regex = re.compile(r"{(?P<escop>{)?(?P<content>[^}]+)}")
ladder_regex = re.compile(r"\[(?P<escop>\[)?(?P<content>[^\]]+)\]")


def krasivo_transformer(text: str) -> str:
    krasivo_text = " ".join([ch.upper() for ch in text if ch.isalnum()])
    return markdown.hcode(krasivo_text)


def ladder_transformer(text: str) -> str:
    return "".join(ch.upper() if idx % 2 == 0 else ch.lower() for idx, ch in enumerate(text))


registered_transformers = (
    Transformer(name="𝓚𝓹𝓪𝓬𝓾𝓫𝓸", transform=krasivo_transformer, regex=krasivo_regex),
    Transformer(name="lAdDeR cAsE", transform=ladder_transformer, regex=ladder_regex),
)


def _transform_part(match, transformer):
    return transformer.transform(match["content"])


def transform(text) -> str:
    clean_text = bleach.clean(text, strip=True)

    transformed = clean_text
    for transformer in registered_transformers:
        transformed = transformer.regex.sub(partial(_transform_part, transformer=transformer), transformed)

    return transformed
