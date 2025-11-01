import pandas as pd
import numpy as np
import random
import datetime
from src.utils import UNIVERSITY, AVATAR_URL, COMMON_DESCRIPTION
from src.helpers.create_data_wrapper import create_data_wrapper
from src.utils.column_setup import TeacherAcademicsConfig
from loguru import logger

@create_data_wrapper
@logger.catch
def create_teacher_academic():
    """
    Create teacher academic data.

    Returns:
        df (pd.DataFrame): teacher academic data.
    """

    df = pd.DataFrame(index= range(TeacherAcademicsConfig.AMOUNT.value))

    # university_name
    df[TeacherAcademicsConfig.UNIVERSITY_NAME.value] = np.random.choice(UNIVERSITY, df.shape[0])

    # academic_major
    df[TeacherAcademicsConfig.ACADEMIC_MAJOR.value] = [f"Test academic major {str(i + 1).zfill(2)}" for i in range(df.shape[0])]

    # academic_period
    current_year = datetime.datetime.now().year
    df["academic_start"] = [random.randint(current_year - 10, current_year) for _ in range(df.shape[0])]
    df["academic_end"] = df["academic_start"] + random.choice(range(3, 10))
    df[TeacherAcademicsConfig.ACADEMIC_PERIOD.value] = df[["academic_start", "academic_end"]].apply(lambda x: f"{x[0]}-{x[1]}", axis=1)
    df.drop(columns=["academic_start", "academic_end"], inplace=True)

    # academic_image_url
    df[TeacherAcademicsConfig.ACADEMIC_IMAGE_URL.value] = AVATAR_URL

    # academic_description
    df[TeacherAcademicsConfig.ACADEMIC_DESCRIPTION.value] = COMMON_DESCRIPTION

    # academic_status
    df[TeacherAcademicsConfig.ACADEMIC_STATUS.value] = TeacherAcademicsConfig.ACADEMIC_STATUS_VALUES.value.get("unverified")

    return df