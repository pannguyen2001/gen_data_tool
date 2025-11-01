import pandas as pd
from src.helpers.create_data_wrapper import create_data_wrapper
from src.utils.column_setup import RoleConfig
from loguru import logger

@create_data_wrapper
@logger.catch
def create_role():
    """
    Create role data.

    Returns:
        df (pandas.DataFrame): A DataFrame containing the new role.
    """
    df = pd.DataFrame(index=range(RoleConfig.AMOUNT.value))

    # name
    df[RoleConfig.NAME.value] = [value for value in RoleConfig.ROLE_VALUES.value]

    return df


