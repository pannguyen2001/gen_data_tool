from src.utils import logger
from src.helpers.logger_wrapper import logger_wrapper

@logger_wrapper
def create_mongodb_collection(db, collection_name: str = "", is_delete_collection: bool = True):
    """ Create MongoDB collection"""

    if is_delete_collection:
        if collection_name in  db.list_collection_names():
            db.drop_collection(collection_name)
            logger.info(f"Deleted collection: {collection_name}")
        else:
            logger.info(f"Collection: {collection_name} does not exist")

    collection = db[collection_name]
    logger.info(f"Created collection: {collection_name}")

    return collection
