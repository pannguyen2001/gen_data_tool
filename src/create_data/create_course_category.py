import pandas as pd
from src.helpers.create_data_wrapper import create_data_wrapper
from src.utils.column_setup import CourseCategoryConfig
from loguru import logger

@create_data_wrapper
@logger.catch
def create_course_category():
    """
    Create course category data.

    Returns:
        df (pd.DataFrame): course category data.
    """

    df = pd.DataFrame(index=range(len(CourseCategoryConfig.TYPE_VALUES.value.values())))

    # type
    df[CourseCategoryConfig.TYPE.value] = CourseCategoryConfig.TYPE_VALUES.value.values()

    # level
    df[CourseCategoryConfig.LEVEL.value] = [list(CourseCategoryConfig.LEVEL_VALUES.value.values())] * df.shape[0]

    # explode data
    df = df.explode(CourseCategoryConfig.TYPE.value, ignore_index=True).explode(CourseCategoryConfig.LEVEL.value, ignore_index=True)

    # description
    df[CourseCategoryConfig.DESCRIPTION.value] = "Test description"

    # status
    df[CourseCategoryConfig.STATUS.value] = CourseCategoryConfig.STATUS_VALUES.value["active"]

    df = df[[
        CourseCategoryConfig.TYPE.value,
        CourseCategoryConfig.LEVEL.value,
        CourseCategoryConfig.DESCRIPTION.value,
        CourseCategoryConfig.STATUS.value
    ]]
    return df