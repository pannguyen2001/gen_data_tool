import random
import string
import datetime
import os
import threading
from loguru import logger

@logger.catch
def generate_enhanced_random_value(length: int = 1) -> str:
    """
    Generate an enhanced random code of specified length.
    For length 1~3, only random characters are used.
    For length >=4, the code is composed of random characters, the last digit of the current timestamp, process ID, and thread ID,
    then shuffled to increase randomness.

    Args:
        length (int): The length of the code to generate.

    Returns:
        str: The generated random code.
    """
    chars = string.ascii_letters + string.digits
    if length <= 3:
        return "".join(random.choices(chars, k=length))
    else:
        # For length >=4, mix random characters, timestamp, process ID, and thread ID
        rand_len = length - 3
        rand_part = "".join(random.choices(chars, k=rand_len))
        ts_part = str(datetime.datetime.now().microsecond)[-1]  # Last digit of timestamp
        pid_part = str(os.getpid())[-1]  # Last digit of process ID
        tid_part = str(threading.get_ident())[-1]  # Last digit of thread ID
        code_list = list(rand_part + ts_part + pid_part + tid_part)
        random.shuffle(code_list)
        return "".join(code_list[:length])
