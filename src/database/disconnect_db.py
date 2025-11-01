from src.utils import logger, DatabaseType
from src.helpers.logger_wrapper import logger_wrapper

# =========== PostgreSQL ===========
@logger_wrapper
def disconnect_postgresql_db(conn):
    conn.close()
    logger.info("Disconnected from PostgreSQL database")

# ========== MongoDB ==========
@logger_wrapper
def disconnect_mongodb_db(db):
    db.client.close()
    logger.info("Disconnected from MongoDB database")


@logger_wrapper
def disconnect_db(db_type: str = DatabaseType.POSTGRESQL.value, connection = None):
    """_summary_: Disconnect from database

    Args:
        db_type (str, optional): _description_. Defaults to DatabaseType.POSTGRESQL.value.
    """

    if db_type == DatabaseType.POSTGRESQL.value:
        disconnect_postgresql_db(connection)
    elif db_type == DatabaseType.MONGODB.value:
        disconnect_mongodb_db(connection)
