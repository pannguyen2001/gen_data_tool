import pandas as pd
import numpy as np
from src.helpers.create_data_wrapper import create_data_wrapper
from src.helpers import get_parent_module_path, create_prequisite_data
from src.utils.column_setup import StudentRatingConfig, CommonColumns
from src.utils import COMMON_DESCRIPTION
from loguru import logger

@create_data_wrapper
@logger.catch
def create_student_rating():
    """
    Create student data.

    Returns:
        df (pd.DataFrame): A dataframe containing the new student rating data.
    """

    parent_module_path = get_parent_module_path(__name__)

    student_func_name = StudentRatingConfig.PREQUISITE_FUNC_NAME.value.get("create_student")
    teacher_func_name = StudentRatingConfig.PREQUISITE_FUNC_NAME.value.get("create_teacher")

    df_student = create_prequisite_data(student_func_name, f"{parent_module_path}.{student_func_name}")
    df_teacher = create_prequisite_data(teacher_func_name, f"{parent_module_path}.{teacher_func_name}")

    df = pd.DataFrame()

    # student_id
    df[StudentRatingConfig.STUDENT_ID.value] = df_student[CommonColumns._ID.value]

    # teacher_id
    df[StudentRatingConfig.TEACHER_ID.value] = [df_teacher[CommonColumns._ID.value]] * df.shape[0]

    df = df.explode(StudentRatingConfig.TEACHER_ID.value, ignore_index=True)

    # rating_content_1
    df[StudentRatingConfig.RATING_CONTENT_1.value] = np.random.uniform(1, 5, df.shape[0]).round(2)

    # rating_content_2
    df[StudentRatingConfig.RATING_CONTENT_2.value] = np.random.uniform(1, 5, df.shape[0]).round(2)

    # rating_content_3
    df[StudentRatingConfig.RATING_CONTENT_3.value] = np.random.uniform(1, 5, df.shape[0]).round(2)

    # rating_content_4
    df[StudentRatingConfig.RATING_CONTENT_4.value] = np.random.uniform(1, 5, df.shape[0]).round(2)

    # rating_avg
    df[StudentRatingConfig.RATING_AVG.value] = (df[StudentRatingConfig.RATING_CONTENT_1.value] + df[StudentRatingConfig.RATING_CONTENT_2.value] + df[StudentRatingConfig.RATING_CONTENT_3.value] + df[StudentRatingConfig.RATING_CONTENT_4.value]) / 4
    df[StudentRatingConfig.RATING_AVG.value] = df[StudentRatingConfig.RATING_AVG.value].round(2)

    # comment
    df[StudentRatingConfig.COMMENT.value] = COMMON_DESCRIPTION

    # is_hidden
    df[StudentRatingConfig.IS_HIDDEN.value] = StudentRatingConfig.IS_HIDDEN_VALUES.value.get("false")

    df = df[[
        StudentRatingConfig.STUDENT_ID.value,
        StudentRatingConfig.TEACHER_ID.value,
        StudentRatingConfig.RATING_AVG.value,
        StudentRatingConfig.RATING_CONTENT_1.value,
        StudentRatingConfig.RATING_CONTENT_2.value,
        StudentRatingConfig.RATING_CONTENT_3.value,
        StudentRatingConfig.RATING_CONTENT_4.value,
        StudentRatingConfig.COMMENT.value,
        StudentRatingConfig.IS_HIDDEN.value
    ]]

    return df

