import pandas as pd
import numpy as np
from loguru import logger
from src.utils.constants import GEN_DATA_AMOUNT, DateTimeFormats

@logger.catch
def generate_random_dates(start: pd.to_datetime = pd.to_datetime('01-01-1920'), end: pd.to_datetime = pd.to_datetime('today'), n: int = GEN_DATA_AMOUNT, date_time_format: str = DateTimeFormats.DATE.value):
    """
    Generate random dates between start and end date.

    Args:
        start (pd.to_datetime, optional): start date. Defaults to pd.to_datetime('01-01-1920').
        end (pd.to_datetime, optional): end date. Defaults to pd.to_datetime('today').
        n (int, optional): size of generated data. Defaults to GEN_DATA_AMOUNT.
        date_time_format (str, optional): datetime format. Defaults to DateTimeFormats.DATE.value.

    Returns:
        pd.Series: generated random dates
    """
    start_u = start.value//10**9
    end_u = end.value//10**9

    if n < 0:
        raise ValueError("Number of random dates requested is less than 0.")
    if start_u > end_u:
        raise ValueError("Start date is greater than end date.")

    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s').strftime(date_time_format)

# start = pd.to_datetime('01-01-1920')
# end = pd.to_datetime('today')
# print(random_dates(start, end))


