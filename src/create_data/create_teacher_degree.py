import pandas as pd
import numpy as np
import random
import datetime
from src.utils import AVATAR_URL, COMMON_DESCRIPTION
from src.helpers.create_data_wrapper import create_data_wrapper
from src.utils.column_setup import TeacherDegreesConfig
from loguru import logger

@create_data_wrapper
@logger.catch
def create_teacher_degree():
    """
    Creates teacher degrees data.

    Returns:
        df (pd.DataFrame): A dataframe of teacher degrees.
    """

    df = pd.DataFrame(index=range(TeacherDegreesConfig.AMOUNT.value))

    # degree_name
    df[TeacherDegreesConfig.DEGREE_NAME.value] = [f"Test degree name {str(i + 1).zfill(2)}" for i in range(df.shape[0])]

    # degree_period
    current_year = datetime.datetime.now().year
    df["degree_start"] = [random.randint(current_year - 10, current_year) for _ in range(df.shape[0])]
    df["degree_end"] = [random.randint(df["degree_start"].iloc[i] + 3, df["degree_start"].iloc[i] + 10) for i in range(df.shape[0])]
    df[TeacherDegreesConfig.DEGREE_PERIOD.value] = df.apply(lambda row: f"{row['degree_start']}-{row['degree_end']}", axis=1)
    df.drop(columns=["degree_start", "degree_end"], inplace=True)

    # degree_level
    df[TeacherDegreesConfig.DEGREE_LEVEL.value] = np.random.choice(TeacherDegreesConfig.DEGREE_LEVEL_VALUES.value, df.shape[0])

    # degree_image_url
    df[TeacherDegreesConfig.DEGREE_IMAGE_URL.value] = AVATAR_URL

    # degree_description
    df[TeacherDegreesConfig.DEGREE_DESCRIPTION.value] = COMMON_DESCRIPTION

    # degree_status
    df[TeacherDegreesConfig.DEGREE_STATUS.value] = TeacherDegreesConfig.DEGREE_STATUS_VALUES.value.get("unverified")

    return df