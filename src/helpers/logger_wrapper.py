import traceback
from functools import wraps
from typing import Callable
from src.utils.logging import logger

def logger_wrapper(func: Callable) -> Callable:
    """
    A decorator wraps a function and provide error logging.
    If the wrap function raises an exception, the decorator will log the error message through logger

    Args:
        func (Callable): the function to be wrapped.

    Returns:
        Callable: the wrapped function with error logging
    """

    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            tb = "".join(traceback.format_tb(e.__traceback__))
            logger.error(f"{func.__name__} has error:\n{tb}")
            return None

    return wrap
