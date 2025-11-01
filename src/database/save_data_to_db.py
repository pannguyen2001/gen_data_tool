import pandas as pd
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.dialects.postgresql import UUID
from src import logger
from src.helpers import logger_wrapper
from src.utils import SCHEMA, PG_URL, CommonColumns, DatabaseType
from src.database.create_mongodb_collection import create_mongodb_collection
from src.utils.cache_store import get_cached_df, ttl_cache
# from loguru import logger

@logger_wrapper
def check_generate_data(df: pd.DataFrame = None):
        """_summary_: Check if generate data function is called

        Returns:
            bool: _description_
        """
        if df is not None and not df.empty:
                check_generate_full_data = CommonColumns.IS_DELETED.value in df.columns
                if  check_generate_full_data:
                        return True
                else:
                        logger.error("Generate common data failed")
                        return False
        else:
                logger.error("Generate data failed")
                return False

# @logger.catch
@logger_wrapper
def save_data_to_postgres_db(df: pd.DataFrame = None, table_name: str = "", is_clear_table: bool = True):
        """_summary_: Save data to PostgreSQL database

        Args:
            df (pd.DataFrame, optional): _description_. Defaults to None.
            table_name (str, optional): _description_. Defaults to "".
            is_clear_table (bool, optional): _description_. Defaults to False.
        """

        try:
                logger.info(f"Saving data to PostgreSQL database, table: {table_name}")
                # logger.info(df)

                if check_generate_data(df):
                        engine = create_engine(PG_URL)

                        if is_clear_table:
                                insp = inspect(engine)
                                if insp.has_table(table_name=table_name, schema=SCHEMA):
                                        with engine.connect() as conn:
                                                conn.execute(text(f'TRUNCATE TABLE {SCHEMA}.{table_name}'))
                                                conn.commit()
                                        logger.info(f"Table: {table_name} is truncated in PostgreSQL database")
                                else:
                                        logger.info(f"Table: {table_name} does not exist in PostgreSQL database")

                        df.to_sql(
                                table_name,
                                con=engine,
                                schema=SCHEMA,
                                if_exists='replace',
                                index=False,
                                dtype={col: UUID(as_uuid=True) for col in df.columns if "_id" in col})

                        logger.info("Saving data to PostgreSQL database successfully")

                        return True
                else:
                        logger.error("Generate data failed, so not save to PostgreSQL database")
                        return False

        except Exception as e:
                logger.error(f"Error occurred while saving data to PostgreSQL database: {e}")

                return False

# @logger.catch
@logger_wrapper
def save_data_to_mongodb_db(db, df: pd.DataFrame = None, collection_name: str = "", is_clear_collection: bool = True):
        """_summary_: Save data to MongoDB database

        Args:
            df (pd.DataFrame, optional): _description_. Defaults to None.
            collection_name (str, optional): _description_. Defaults to "".
            is_clear_collection (bool, optional): _description_. Defaults to False.
        """
        try:
                logger.info(f"Saving data to MongoDB database, collection: {collection_name}")

                if check_generate_data(df):
                        collection = create_mongodb_collection(db, collection_name, is_clear_collection)

                        collection.insert_many(df.to_dict('records'))

                        logger.info("Saving data to MongoDB database successfully")

                        return True
                else:
                        logger.error("Generate data failed, so not save to MongoDB database")

                        return False

        except Exception as e:
                logger.error(f"Error occurred while saving data to MongoDB database: {e}")

                return False

@logger_wrapper
def save_data_to_db(db_type: str = "", mongo_db = None, is_drop: bool = True):
        """_summary_: Save data to PostgreSQL and MongoDB database

        Args:
            db_type (str, optional): _description_. Defaults to "".
            mongo_db (MongoClient, optional): _description_. Defaults to None.
            is_drop (bool, optional): _description_. Defaults to False.

        Returns:
            None: _description_
        """

        if db_type == DatabaseType.POSTGRESQL.value:
                for table in ttl_cache.keys():
                        table_name = table.replace("create_", "")
                        save_data_to_postgres_db(df=get_cached_df(table), table_name=table_name, is_clear_table=is_drop)
        elif db_type == DatabaseType.MONGODB.value:
                for collection in ttl_cache.keys():
                        collection_name = collection.replace("create_", "")
                        save_data_to_mongodb_db(db=mongo_db, df=get_cached_df(collection), collection_name=collection_name, is_clear_collection=is_drop)
        else:
                logger.error("Database type is not supported")