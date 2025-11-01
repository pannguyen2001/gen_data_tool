from sqlalchemy import text, schema
from src.utils import logger
from src.helpers import logger_wrapper

@logger_wrapper
def create_postgresql_db(engine, db_name, schema_name):
    """_summary_: Create database if not exists

    Args:
        engine (_type_): _description_
        db_name (_type_): _description_
        schema (_type_): _description_

    Returns:
        _type_: _description_
    """
    with engine.connect() as connection:
        # Check for DB existence
        result = connection.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
            {"dbname": db_name}
        )
        if result.scalar() is None:
            connection.execution_options(isolation_level="AUTOCOMMIT").execute(
                text(f'CREATE DATABASE "{db_name}"')
            )
            logger.info(f"✅ Created database: {db_name}")
        else:
            logger.info(f"ℹ️ Database already exists: {db_name}")

        # ✅ Create schema (idempotent)
        if not connection.dialect.has_schema(connection, schema_name):
            connection.execute(schema.CreateSchema(schema_name,if_not_exists=True))
            connection.commit()
            logger.info(f"✅ Created schema: {schema_name}")
        else:
            logger.info(f"ℹ️ Schema already exists: {schema_name}")