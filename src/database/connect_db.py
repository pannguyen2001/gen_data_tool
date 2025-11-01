import psycopg2
from sqlalchemy import create_engine
from psycopg2 import sql
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from src.utils import logger, PG_URL, PG_DB, PG_HOST, PG_PORT, PG_USERNAME, PG_PASSWORD, MONGODB_URL, MONGODB_DATABASE, MONGODB_USERNAME, SCHEMA, DatabaseType
from src.helpers.logger_wrapper import logger_wrapper
from src.database.create_postgresql_db import create_postgresql_db

# =========== PostgreSQL ===========
@logger_wrapper
def connect_postgresql_db():
    """ Connect to PostgreSQL database"""
    conn = psycopg2.connect(
        host=PG_HOST,
        database=PG_DB,
        user=PG_USERNAME,
        password=PG_PASSWORD,
        port=PG_PORT,
        options='-c client_encoding=UTF8'
        )
    conn.set_client_encoding('UTF8')
    conn.autocommit = True

    logger.info(f"Connected to PostgreSQL database. Database name: {PG_DB}, host: {PG_HOST}, port: {PG_PORT}, username: {PG_USERNAME}")

    return conn

# ========== MongoDB ==========
@logger_wrapper
def connect_mongodb_db():
    """ Connect to MongoDB database"""
    client = MongoClient(MONGODB_URL,server_api=ServerApi('1'))
    db = client[MONGODB_DATABASE]
    logger.info(f"Connected to MongoDB database. Database name: {MONGODB_DATABASE}, host: {MONGODB_URL}, username: {MONGODB_USERNAME}")

    return db

@logger_wrapper
def connnect_db(db_type: str = DatabaseType.POSTGRESQL.value):
    """_summary_: Connect to database

    Args:
        db_type (str, optional): _description_. Defaults to DatabaseType.POSTGRESQL.value.
    """

    connection = None

    if db_type == DatabaseType.POSTGRESQL.value:
        connection = connect_postgresql_db()
        engine = create_engine(PG_URL)
        create_postgresql_db(engine, PG_DB, SCHEMA)
    elif db_type == DatabaseType.MONGODB.value:
        connection = connect_mongodb_db()
    else:
        logger.error(f"Invalid database type: {db_type}")

    return connection


# conn = psycopg2.connect(
#         host= os.environ.get("POSTGRESQL_HOST"),
#         database= os.environ.get("POSTGRESQL_DB"),
#         user= os.environ.get("POSTGRESQL_USER"),
#         password= os.environ.get("POSTGRESQL_PASSWORD"),
#         port= os.environ.get("POSTGRESQL_PORT"))
# cur = conn.cursor()
# cur.execute("SELECT * FROM public.ratings LIMIT 10")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# cur.close()
# conn.close()
# print("Done")

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Update with your PostgreSQL credentials
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pgpwd@localhost:5432/postgres'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Example model (match table in your DB like 'account')
# class Account(db.Model):
#     __tablename__ = 'account'
#     user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String())
#     email = db.Column(db.String())

#     def __repr__(self):
#         return f'<Account {self.username}>'

# @app.route('/')
# def index():
#     accounts = Account.query.all()
#     print(accounts[0].username)
#     return '<br>'.join(str(acc) for acc in accounts)

# if __name__ == '__main__':
#     app.run(debug=True)