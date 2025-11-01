import pandas as pd
from src.helpers.create_data_wrapper import create_data_wrapper
from src.helpers import get_parent_module_path, create_prequisite_data
from src.utils.column_setup import AccountConfig, StudentConfig, RoleConfig, CommonColumns
from src.utils.cache_store import get_cached_df
from loguru import logger

@create_data_wrapper
@logger.catch
def create_student():
    """
    Create student data.

    Returns:
        df (pd.DataFrame): A dataframe containing the new student data.
    """
    # Get the path to the parent module
    parent_module_path = get_parent_module_path(__name__)

    account_func_name = StudentConfig.PREQUISITE_FUNC_NAME.value.get("create_account")
    role_func_name = StudentConfig.PREQUISITE_FUNC_NAME.value.get("create_role")

    df_account = create_prequisite_data(account_func_name, f"{parent_module_path}.{account_func_name}")

    df = pd.DataFrame()

    # account_id
    # Get account_id of students from the cached dataframe
    df_role = get_cached_df(role_func_name)

    if df_role is None:
        raise Exception("Failed to get role data")

    student_role_id = df_role[df_role[RoleConfig.NAME.value] == RoleConfig.ROLE_VALUES.value.get("student")][CommonColumns._ID.value].values[0]

    student_account_id = df_account[df_account[AccountConfig.ROLE_ID.value] == student_role_id][CommonColumns._ID.value].values

    df[StudentConfig.ACCOUNT_ID.value] = student_account_id

    # rating_teacher_ids
    df[StudentConfig.RATING_TEACHER_IDS.value] = [[]] * df.shape[0]

    df = df[[
        StudentConfig.ACCOUNT_ID.value,
        StudentConfig.RATING_TEACHER_IDS.value
    ]]

    return df
