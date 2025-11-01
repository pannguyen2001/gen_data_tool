import pandas as pd
from src.helpers.create_data_wrapper import create_data_wrapper
from src.helpers import get_parent_module_path, create_prequisite_data
from src.utils.column_setup import CourseStudentConfig, CommonColumns
from loguru import logger

@create_data_wrapper
@logger.catch
def create_course_student():
    """
    Create course student data.

    Returns:
        df (pd.DataFrame): A dataframe containing the new course student relates data.
    """

    parent_module_path = get_parent_module_path(__name__)
    course_func_name = CourseStudentConfig.PREQUISITE_FUNC_NAME.value.get("create_course")
    student_func_name = CourseStudentConfig.PREQUISITE_FUNC_NAME.value.get("create_student")

    df_course = create_prequisite_data(course_func_name, f"{parent_module_path}.{course_func_name}")
    df_student = create_prequisite_data(student_func_name, f"{parent_module_path}.{student_func_name}")

    df = pd.DataFrame()

    # course_id
    df[CourseStudentConfig.COURSE_ID.value] = df_course[CommonColumns._ID.value]

    # student_id
    df[CourseStudentConfig.STUDENT_ID.value] = [df_student[CommonColumns._ID.value].values.tolist()] * df.shape[0]

    # df = df.explode(CourseStudentConfig.STUDENT_ID.value, ignore_index=True)

    df = df[[
        CourseStudentConfig.COURSE_ID.value,
        CourseStudentConfig.STUDENT_ID.value
    ]]

    return df