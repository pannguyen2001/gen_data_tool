import pandas as pd
import importlib
from src.utils.cache_store import get_cached_df
from src.utils import CreateDataResult
from loguru import logger

@logger.catch
def create_prequisite_data(prequisite_cache_key: str = "", prequisite_function_path: str = ""):
    """
    Create prerequisite data for the database.

    Args:
        prequisite_function (str): The name of the function to create prerequisite data.
        prequisite_function_path (str): The path to the function to create prerequisite data.

    Returns:
        df (pandas.DataFrame): The dataframe containing the prerequisite data.

    """

    df = get_cached_df(prequisite_cache_key)

    if df is None:
        module = importlib.import_module(prequisite_function_path)
        create_func = getattr(module, prequisite_cache_key, None)

        if not callable(create_func):
            raise AttributeError(f"{prequisite_cache_key} is not a callable in {prequisite_function_path}")

        create_result = create_func()

        if create_result.get("result") == CreateDataResult.FAIL.value:
            raise Exception(f"Failed to create {prequisite_cache_key}")
        else:
            df = get_cached_df(prequisite_cache_key)

    return df