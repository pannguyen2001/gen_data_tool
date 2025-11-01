from flask import Flask
from src.utils import logger
from src.config import Config
from dotenv import load_dotenv

# loading environment variables
logger.info("Loading environment variables")
load_dotenv()
logger.info("Environment variables loaded successfully")

# declaring flask application
logger.info("Declaring flask application")
app = Flask(__name__)
logger.info("Flask application declared successfully")

# calling the dev configuration
logger.info("Calling the dev configuration")
config = Config().dev_config
logger.info("Dev configuration called successfully")

# making our application to use dev env
app.env = config.ENV