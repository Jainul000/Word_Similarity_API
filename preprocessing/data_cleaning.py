import re
from typing import List

def split_camel_case(text: str) -> str:
    """
    Split camelCase and PascalCase words.
    Example: isPrimeNumber -> is Prime Number
    """
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)


def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9_ ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.split()



