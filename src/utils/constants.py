import pytz
import datetime
import enum
import os
import pandas as pd
from dotenv import load_dotenv

# ========== Enums ==========
class DateTimeFormats(enum.Enum):
    """Enum for date time format"""
    DATE_TIME = "%Y-%m-%d %H:%M:%S"
    DATE = "%Y-%m-%d"
    TIME = "%H:%M:%S"

class AnsiColors(enum.Enum):
    '''Enum for ANSI colors'''
        # ANSI colors
    GREEN = "\x1b[32m"
    BLUE = "\x1b[34m"
    YELLOW = "\x1b[33m"
    RED = "\x1b[31m"
    RESET = "\x1b[0m"
    BOLD = "\x1b[1m"
    UNDERLINE = "\x1b[4m"
    NORMAL = "\x1b[22m"

class CreateDataResult(enum.Enum):
    """Enum for create data result"""
    SUCCESS = "success"
    FAIL = "fail"

class DatabaseType(enum.Enum):
    """Enum for database type"""
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"

# ========== Constants ==========
# Author
author_full_name = "Pham Anh Nhat"
author_email = "truonghoc19102001@gmail.com"

# Logging
is_log_file = True
log_file_path = "src/logs"
console_log_format = f"{AnsiColors.BOLD.value}%(levelname)s{AnsiColors.NORMAL.value} %(filename)s:%(lineno)d\t{AnsiColors.RESET.value}%(message)s "
file_log_format = "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]: %(message)s"

# Datetime
time_zone = "Asia/Ho_Chi_Minh"
tzInfo = pytz.timezone(time_zone)
today = datetime.datetime.strftime(datetime.datetime.now(tz=tzInfo), DateTimeFormats.DATE.value)

# Gen data amount
GEN_DATA_AMOUNT = 5

# Password
PASSWORD = "123456789"

# Avatar url
AVATAR_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNnNH0c03eYhzzID8_Y6mHwZYYGjXLfnreH7RyT9f9GVRtT0yR7vklbKx3As07G6DCGYY&usqp=CAU"

# Common descrition
COMMON_DESCRIPTION = "This is a common description from the data generator"

# Database info
SCHEMA = "renew_capstone_project"
DB_TYPE = DatabaseType.MONGODB.value

load_dotenv()

# PostgreSQL
PG_URL = os.getenv("POSTGRESQL_URL")
PG_HOST = os.getenv("POSTGRESQL_HOST")
PG_PORT = os.getenv("POSTGRESQL_PORT")
PG_USERNAME = os.getenv("POSTGRESQL_USERNAME")
PG_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
PG_DB = os.getenv("POSTGRESQL_DB")

# MongoDB
MONGODB_URL = os.environ.get("MONGODB_URL")
MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")

# ========== Get data from storage ==========
# Email domain
EMAIL_DOMAIN = pd.read_csv("src/data/email_domain.csv")["Email domain"].tolist()

# University name
UNIVERSITY = pd.read_csv("src/data/university.csv")["University"].tolist()

# VN province
PROVINCE = pd.read_csv("src/data/province_2025.csv")["Province/city"].tolist()


