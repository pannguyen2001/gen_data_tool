from enum import Enum
from src.utils import GEN_DATA_AMOUNT

class CommonConfig:
    def __init__(self, table_name: str = "", columns: Enum = None, amount: int = GEN_DATA_AMOUNT, **kwargs):
        self.table_name = table_name
        self.columns = columns
        self.amount = amount


class CommonColumns(Enum):
    _ID = "_id"
    CREATED_ON = "created_on"
    MODIFIED_ON = "modified_on"
    CREATED_BY = "created_by"
    MODIFIED_BY = "modified_by"
    IS_DELETED = "is_deleted"

    IS_DELETED_VALUES = {
        "true": True,
        "false": False
    }
    CREATED_BY_VALUES = MODIFIED_BY_VALUES = {
        "admin": "admin",
        "teacher": "teacher",
        "student": "student",
        "data_generation": "data generation"
    }


class RoleConfig(Enum):
    """Enum for roles table"""

    # Table Info
    TABLE_NAME = "roles"
    AMOUNT = 3

    # Column names
    NAME = "name"

    # Dropdown values
    ROLE_VALUES = {
            "admin": "admin",
            "teacher": "teacher",
            "student": "student"
        }

class AccountConfig(Enum):
    """Enum for accounts table"""

    # Table Info
    TABLE_NAME = "accounts"
    AMOUNT = {
        "admin": 1,
        "teacher": GEN_DATA_AMOUNT,
        "student": GEN_DATA_AMOUNT
    }

    # Prequisite
    CREATE_ROLE = "create_role"

    # Column names
    ROLE_ID = "role_id"
    FULL_NAME = "full_name"
    DATE_OF_BIRTH = "date_of_birth"
    GENDER = "gender"
    ADDRESS = "address"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    PASSWORD = "password"
    AVATAR_URL = "avatar_url"
    STATUS = "status"

    # Dropdown values
    GENDER_VALUES = {
            "male": "male",
            "female": "female",
            "other": "other"
    }
    STATUS_VALUES = {
            "active": "active",
            "inactive": "inactive",
            "blocked": "blocked",
            "deleted": "deleted"
    }

class StudentConfig(Enum):
    """Enum for students table"""

    # Table Info
    TABLE_NAME = "students"

    # Prequisite
    PREQUISITE_FUNC_NAME = {
        "create_role": "create_role",
        "create_account": "create_account"
    }

    # Column names
    ACCOUNT_ID = "account_id"
    RATING_TEACHER_IDS = "rating_teacher_ids"

class CourseCategoryConfig(Enum):
    """Enum for course category table"""

    # Table Info
    TABLE_NAME = "coursecategories"

    # Column names
    TYPE = "type"
    LEVEL = "level"
    DESCRIPTION = "description"
    STATUS = "status"

    # Dropdown values
    TYPE_VALUES = {
        "toeic": "toeic",
        "ielts": "ielts",
        "toefl": "toefl",
        "other": "other"
    }
    LEVEL_VALUES = {
        "beginner": "beginner",
        "intermediate": "intermediate",
        "advanced": "advanced",
    }
    STATUS_VALUES = {
        "active": "active",
        "inactive": "inactive"
    }

class CourseConfig(Enum):
    """Enum for courses table"""

    # Table Info
    TABLE_NAME = "courses"
    AMOUNT = GEN_DATA_AMOUNT

    PREQUISITE_FUNC_NAME = {
        "create_course_category":
        "create_course_category",
        "create_teacher": "create_teacher"
    }

    # Column names
    CATEGORY_ID = "category_id"
    TEACHER_ID = "teacher_id"
    NAME = "name"
    DESCRIPTION = "description"
    STUDENT_AMOUNT = "student_amount"
    SCHEDULE = "schedule"
    START_DATE = "start_date"
    END_DATE = "end_date"
    STATUS = "status"
    TIME_PER_LESSION = "time_per_lesson"
    PRICE = "price"

    # Dropdown values
    WEEKDAY_VALUES = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    STATUS_VALUES = {
        "not_started": "not started",
        "started": "started",
        "finished": "finished",
        "cancelled": "cancelled"
    }

class CourseStudentConfig(Enum):
    """Enum for course student table"""

    # Table Info
    TABLE_NAME = "coursestudents"

    # Prequisite
    PREQUISITE_FUNC_NAME = {
        "create_course": "create_course",
        "create_student": "create_student"
    }

    # Column names
    COURSE_ID = "course_ids"
    STUDENT_ID = "student_ids"

class StudentRatingConfig(Enum):
    """Enum for student rating table"""

    # Table Info
    TABLE_NAME = "studentratings"

    # Prequisite
    PREQUISITE_FUNC_NAME = {
        "create_student": "create_student",
        "create_teacher": "create_teacher",
    }

    # Column names
    STUDENT_ID = "student_id"
    TEACHER_ID = "teacher_id"
    RATING_AVG = "rating_avg"
    RATING_CONTENT_1 = "rating_content_1"
    RATING_CONTENT_2 = "rating_content_2"
    RATING_CONTENT_3 = "rating_content_3"
    RATING_CONTENT_4 = "rating_content_4"
    COMMENT = "comment"
    IS_HIDDEN = "is_hidden"

    # Dropdown values
    IS_HIDDEN_VALUES = {
        "true": True,
        "false": False
    }

class TeacherConfig(Enum):
    """Enum for teachers table"""

    # Table Info
    TABLE_NAME = "teachers"
    AMOUNT = GEN_DATA_AMOUNT

    # Prequisite
    PREQUISITE_FUNC_NAME = {
        "create_role": "create_role",
        "create_account": "create_account",
        "create_teacher_academic": "create_teacher_academic",
        "create_teacher_degree": "create_teacher_degree"
    }

    # Column names
    ACCOUNT_ID = "account_id"
    PERSONAL_DESCRIPTION = "personal_description"
    PERSONAL_IMAGE_URL = "personal_image_url"
    # STUDENT_RATING_IDS = "student_rating_ids"
    # COURSE_IDS = "course_ids"
    ACADEMIC_IDS = "academic_ids"
    DEGREE_IDS = "degree_ids"


class TeacherAcademicsConfig(Enum):
    """Enum for teacher academics table"""

    # Table Info
    TABLE_NAME = "teacheracademics"
    AMOUNT = GEN_DATA_AMOUNT

    # Column names
    UNIVERSITY_NAME = "university_name"
    ACADEMIC_MAJOR = "academic_major"
    ACADEMIC_PERIOD = "academic_period"
    ACADEMIC_IMAGE_URL = "academic_image_url"
    ACADEMIC_DESCRIPTION = "academic_description"
    ACADEMIC_STATUS = "academic_status"

    # Dropdown values
    ACADEMIC_STATUS_VALUES = {
        "unverified": "unverified",
        "verifying": "verifying",
        "verified": "verified",
        "can_not_verify": "can not verify"
    }

class TeacherDegreesConfig(Enum):
    """Enum for teacher degrees table"""

    # Table Info
    TABLE_NAME = "teacherdegrees"
    AMOUNT = GEN_DATA_AMOUNT

    # Column names
    DEGREE_NAME = "degree_name"
    DEGREE_PERIOD = "degree_period"
    DEGREE_LEVEL = "degree_level"
    DEGREE_IMAGE_URL = "degree_image_url"
    DEGREE_DESCRIPTION = "degree_description"
    DEGREE_STATUS = "degree_status"

    # Dropdown values
    DEGREE_STATUS_VALUES = {
        "unverified": "unverified",
        "verifying": "verifying",
        "verified": "verified",
        "can_not_verify": "can not verify"
    }
    DEGREE_LEVEL_VALUES = ["Associate", "Bachelor", "Master", "Doctor"]
