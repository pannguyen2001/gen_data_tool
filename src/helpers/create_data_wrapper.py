import timeit
import datetime
from pathlib import Path
from functools import wraps
from typing import Callable
from .logger_wrapper import logger_wrapper
from src.helpers import generate_id
from src.helpers.create_result import Result
from src.utils import DB_TYPE
from src.utils.column_setup import CommonColumns
from src.utils.constants import DateTimeFormats, tzInfo, CreateDataResult
from src.utils.logging import logger
from src.utils.cache_store import cache_df, invalidate_cache

@logger_wrapper
def create_data_wrapper(func: Callable) -> Callable:
    """
    A decorator wraps a create data function, create common columns, save to database and provide error logging.
    If the wrap function raises an exception, the decorator will log the error message through logger.
    The decorator will also log the start and end time of the wrapped function.

    Args:
        func (Callable): the function to be wrapped.

    Returns:
        result (Result): the result of the wrapped function.
    """

    result = Result()
    result.file = Path(func.__name__).as_posix()
    cache_key = func.__name__

    @wraps(func)
    def wrap(*args, **kwargs):
        logger.info(f"Start creating data for {func.__name__}")
        result.start = timeit.default_timer()

        try:
            df = func(*args, **kwargs)

            if df is not None:
                df[CommonColumns.IS_DELETED.value] = CommonColumns.IS_DELETED_VALUES.value["false"]

                df[CommonColumns.CREATED_ON.value] = df[CommonColumns.MODIFIED_ON.value] = df[CommonColumns.CREATED_BY.value] = datetime.datetime.strftime(datetime.datetime.now(tz=tzInfo), DateTimeFormats.DATE_TIME.value)

                df[CommonColumns.CREATED_BY.value] = df[CommonColumns.MODIFIED_BY.value] = CommonColumns.CREATED_BY_VALUES.value["data_generation"]

                _id = generate_id(db_type=DB_TYPE, size=df.shape[0])
                df.insert(0, CommonColumns._ID.value, _id)

                cache_df(cache_key, df)

        except Exception as e:
            logger.error(f"{func.__name__} has error: {e}")
            result.result = CreateDataResult.FAIL.value
            result.error = e
            invalidate_cache(cache_key)

        finally:
            result.end = timeit.default_timer()
            logger.info(f"Finish creating data for {func.__name__}")

        return result.__dict__()

    return wrap

                # if df is not None and not df.empty:
                #     check_generate_full_data = CommonColumns.IS_DELETED.value in df.columns
                #     if  check_generate_full_data:
                #         table_name = func.__name__.replace("create_", "")
                #         save_result = False
                #         if kwargs["db_type"] == DatabaseType.POSTGRESQL.value:
                #             save_result = save_data_to_postgres_db(df, table_name)
                #         else:
                #             save_result = save_data_to_mongodb_db(kwargs["mongo_db"], df, table_name)

                #         if save_result:
                #             # cahche dataframe
                #             cache_df(cache_key, df)
                #         else:
                #             invalidate_cache(cache_key)
                #     else:
                #         logger.error("Generate common data failed")
                #         invalidate_cache(cache_key)
                # else:
                #     logger.error("Generate data failed")
                #     invalidate_cache(cache_key)