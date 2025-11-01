import bcrypt
from src.utils import PASSWORD
from loguru import logger

@logger.catch
def generate_hash_password(password: str = PASSWORD, password_len: int = 10, encode_type: str = "utf-8", data_size: int = 1) -> str:
    """
    Generate a hashed password using the PASSWORD constant from the utils module.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """

    # Converting password to array of bytes
    bytes = password.encode(encode_type)

    # Hashing the password
    result = [bcrypt.hashpw(bytes, bcrypt.gensalt(password_len)).decode("utf-8") for _ in range(data_size)]

    return result