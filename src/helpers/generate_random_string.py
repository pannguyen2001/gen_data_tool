import string
import random
from loguru import logger

@logger.catch
def generate_random_string(length: int = 10) -> str:
    """
    Generate a random string of specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))