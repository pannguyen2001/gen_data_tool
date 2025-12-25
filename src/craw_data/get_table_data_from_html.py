import pandas as pd
from src.helpers import logger_wrapper

@logger_wrapper
def get_table_data_from_html(url: str = "", **kwargs) -> pd.DataFrame | None:
    """
    Get table data from html.

    Args:
        url (str): The url of the html.
        **kwargs: The keyword arguments.

    Returns:
        df (pd.DataFrame): The dataframe of the table.
    """
    df = pd.read_html(url, **kwargs)
    return df