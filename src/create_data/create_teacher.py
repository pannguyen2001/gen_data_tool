import pandas as pd
from src.helpers.create_data_wrapper import create_data_wrapper
from src.helpers import get_parent_module_path, create_prequisite_data
from src.utils.column_setup import TeacherConfig, RoleConfig, AccountConfig, CommonColumns
from src.utils.cache_store import get_cached_df
from src.utils import COMMON_DESCRIPTION
from loguru import logger

@create_data_wrapper
@logger.catch
def create_teacher():
    """
    Create teacher data.

    Returns:
        df (pd.DataFrame): A dataframe containing the new teacher data.
    """

    parent_module_path = get_parent_module_path(__name__)

    account_func_name = TeacherConfig.PREQUISITE_FUNC_NAME.value.get("create_account")
    role_func_name = TeacherConfig.PREQUISITE_FUNC_NAME.value.get("create_role")
    teacher_academic_func_name = TeacherConfig.PREQUISITE_FUNC_NAME.value.get("create_teacher_academic")
    teacher_degree_func_name = TeacherConfig.PREQUISITE_FUNC_NAME.value.get("create_teacher_degree")

    df_account = create_prequisite_data(account_func_name, f"{parent_module_path}.{account_func_name}")
    df_teacher_academic = create_prequisite_data(teacher_academic_func_name, f"{parent_module_path}.{teacher_academic_func_name}")
    df_teacher_degree = create_prequisite_data(teacher_degree_func_name, f"{parent_module_path}.{teacher_degree_func_name}")

    df = pd.DataFrame()

    # account_id
    df_role = get_cached_df(role_func_name)

    if df_role is None:
        raise Exception("Failed to get role data")

    teacher_role_id = df_role[df_role[RoleConfig.NAME.value] == RoleConfig.ROLE_VALUES.value.get("teacher")][CommonColumns._ID.value].values[0]

    teacher_account_id = df_account[df_account[AccountConfig.ROLE_ID.value] == teacher_role_id][CommonColumns._ID.value].values

    df[TeacherConfig.ACCOUNT_ID.value] = teacher_account_id

    # personal_description
    df[TeacherConfig.PERSONAL_DESCRIPTION.value] = COMMON_DESCRIPTION

    # personal_image_url
    df[TeacherConfig.PERSONAL_IMAGE_URL.value] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNnNH0c03eYhzzID8_Y6mHwZYYGjXLfnreH7RyT9f9GVRtT0yR7vklbKx3As07G6DCGYY&usqp=CAU"

    # academic_ids
    df[TeacherConfig.ACADEMIC_IDS.value] = df_teacher_academic[CommonColumns._ID.value]

    # degree_ids
    df[TeacherConfig.DEGREE_IDS.value] = df_teacher_degree[CommonColumns._ID.value]

    # Reorder columns
    df = df[[
        TeacherConfig.ACCOUNT_ID.value,
        TeacherConfig.PERSONAL_DESCRIPTION.value,
        TeacherConfig.PERSONAL_IMAGE_URL.value,
        TeacherConfig.ACADEMIC_IDS.value,
        TeacherConfig.DEGREE_IDS.value
        ]]

    return df