import string
import random
from loguru import logger

@logger.catch
def generate_special_chars(length: int = 10, additional_chars: str = "", except_chars: str = "") -> str:
    """"""
    chars = string.punctuation
    if additional_chars:
        chars += additional_chars
    if except_chars:
        chars = "".join([c for c in chars if c not in except_chars])
    
    return "".join(random.choices(chars, k=length))