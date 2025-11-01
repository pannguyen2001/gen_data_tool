from loguru import logger

@logger.catch
def get_parent_module_path(module_path: str) -> str:
    """
    Get the parent module path of a given module path.

    Args:
        module_path (str): The module path.

    Returns:
        str: The parent module path.
    """
    return ".".join(module_path.split(".")[:-1]) or "__main__"