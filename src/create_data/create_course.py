import pandas as pd
import random
from src.helpers.create_data_wrapper import create_data_wrapper
from src.helpers import get_parent_module_path, generate_random_dates, create_prequisite_data
from src.utils.column_setup import CourseConfig, TeacherConfig, CommonColumns
from src.utils import COMMON_DESCRIPTION, DateTimeFormats
from loguru import logger

@create_data_wrapper
@logger.catch
def create_course():
    """
    Create course data.

    Returns:
        df (pd.DataFrame): A dataframe containing the new course data.
    """

    parent_module_path = get_parent_module_path(__name__)
    course_category_func_name = CourseConfig.PREQUISITE_FUNC_NAME.value.get("create_course_category")
    teacher_func_name = CourseConfig.PREQUISITE_FUNC_NAME.value.get("create_teacher")

    df_category = create_prequisite_data(course_category_func_name, f"{parent_module_path}.{course_category_func_name}")
    df_teacher = create_prequisite_data(teacher_func_name, f"{parent_module_path}.{teacher_func_name}")

    df = pd.DataFrame()

    # category_id
    df[CourseConfig.CATEGORY_ID.value] = df_category[CommonColumns._ID.value]

    # teacher_id
    df[CourseConfig.TEACHER_ID.value] = [df_teacher[CommonColumns._ID.value].values.tolist()] * df.shape[0]

    df = df.explode(CourseConfig.TEACHER_ID.value, ignore_index=True)

    # name
    df[CourseConfig.NAME.value] = [f"Course {str(i + 1).zfill(2)}" for i in range(df.shape[0])]

    # description
    df[CourseConfig.DESCRIPTION.value] = COMMON_DESCRIPTION

    # student_amount
    df[CourseConfig.STUDENT_AMOUNT.value] = [random.randrange(10, 100) for _ in range(df.shape[0])]

    # schedule
    df["weekday"] = [random.choice(list(CourseConfig.WEEKDAY_VALUES.value)) for _ in range(df.shape[0])]

    df[CourseConfig.SCHEDULE.value] = df["weekday"] + " - " + generate_random_dates(date_time_format=DateTimeFormats.TIME.value, n=df.shape[0])
    df.drop("weekday", axis=1, inplace=True)

    # time_per_lesson
    df[CourseConfig.TIME_PER_LESSION.value] = [random.randrange(45, 120) for _ in range(df.shape[0])]

    # start_date
    df[CourseConfig.START_DATE.value] = generate_random_dates(start=pd.to_datetime("2025-01-01"),end=pd.to_datetime("2025-12-31"), date_time_format=DateTimeFormats.DATE.value, n=df.shape[0])

    # end_date
    df[CourseConfig.END_DATE.value] = (pd.to_datetime(df[CourseConfig.START_DATE.value]) + pd.to_timedelta(60, unit='d')).astype(str)

    # status
    df[CourseConfig.STATUS.value] = [random.choice(list(CourseConfig.STATUS_VALUES.value.values())) for _ in range(df.shape[0])]

    # price
    df[CourseConfig.PRICE.value] = [random.randrange(50_000, 50_000_000,1_000) for _ in range(df.shape[0])]

    df = df[[
        CourseConfig.CATEGORY_ID.value,
        CourseConfig.TEACHER_ID.value,
        CourseConfig.NAME.value,
        CourseConfig.DESCRIPTION.value,
        CourseConfig.STUDENT_AMOUNT.value,
        CourseConfig.SCHEDULE.value,
        CourseConfig.TIME_PER_LESSION.value,
        CourseConfig.START_DATE.value,
        CourseConfig.END_DATE.value,
        CourseConfig.STATUS.value,
        CourseConfig.PRICE.value
    ]]

    return df