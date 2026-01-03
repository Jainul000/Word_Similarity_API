import re

CAMEL_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')
NON_ALPHA_PATTERN = re.compile(r'[^a-zA-Z\s]+')


def split_camel_case(text: str) -> str:
    return CAMEL_PATTERN.sub(' ', text)


def normalize_text(text: str) -> str:
    text = text.lower()
    text = split_camel_case(text)
    text = text.replace('_', ' ')
    text = NON_ALPHA_PATTERN.sub(' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
