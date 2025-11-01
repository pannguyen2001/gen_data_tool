import pandas as pd
from src.helpers import logger_wrapper

@logger_wrapper
def get_table_data_from_html(url: str = "", **kwargs):
    """
    """
    df = pd.read_html(url, **kwargs)
    return df