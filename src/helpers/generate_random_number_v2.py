import random
from loguru import logger

@logger.catch
def generate_random_number_v2(lower_range: int | float = 0, upper_range: int | float = 1_000_000, type_data = "int") -> int | float:
    """
    Generate a random number between lower_range and upper_range.

    Args:
        lower_range (int | float): The lower range of the random number.
        upper_range (int | float): The upper range of the random number.
        type_data (str): The type of the random number.

    Returns:
        int | float: The random number.
    """

    if type_data == "int":
        return random.randint(lower_range, upper_range)
    else:
        return random.uniform(lower_range, upper_range)