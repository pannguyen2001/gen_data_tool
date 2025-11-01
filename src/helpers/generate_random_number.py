import datetime
from loguru import logger

@logger.catch
def generate_random_number(amount: int = 1) -> int:
        """
        Generate an random number

        Args:
            length (int): Amount of number.

        Returns:
            str: The generated random code.
        """
        current_date_time = datetime.datetime.now()
        random_str = str(int(current_date_time.timestamp()) + int(current_date_time.microsecond))
        if len(random_str) <= amount:
            random_str = (random_str * (amount//len(random_str) + 1))[:amount]
        else:
            random_str = random_str[len(random_str) - amount:]
        random_number = int(random_str)

        return random_number
