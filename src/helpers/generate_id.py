import uuid
from bson import ObjectId
from loguru import logger
from src.utils import DatabaseType

@logger.catch
def generate_uuid(size: int = 1) -> list:
    """Generate a series of UUIDs.

    Args:
        size (int, optional): Number of UUIDs to generate. Defaults to 1.

    Returns:
        list: list of UUIDs.
    """
    return [uuid.uuid4() for _ in range(size)]

@logger.catch
def generate_object_id(size: int = 1) -> list:
    """Generate a series of Object IDs.

    Args:
        size (int, optional): Number of object IDs to generate. Defaults to 1.

    Returns:
        list: list of Object IDs.
    """
    return [ObjectId() for _ in range(size)]

@logger.catch
def generate_id(db_type: str = DatabaseType.POSTGRESQL.value, size: int = 1) -> list:
    """Generate a series of IDs.

    Args:
        db_type (str, optional): Type of database. Defaults to DB_TYPE.

    Returns:
        list: list of IDs.
    """
    if db_type == DatabaseType.POSTGRESQL.value:
        return generate_uuid(size)
    elif db_type == DatabaseType.MONGODB.value:
        return generate_object_id(size)
    else:
        raise ValueError(f"Invalid database type: {db_type}")