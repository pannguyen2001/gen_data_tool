"""
GG search key: delete file python
Solution: https://stackoverflow.com/questions/6996603/how-can-i-delete-a-file-or-folder-in-python
"""

import pathlib
from .logger_wrapper import logger

def delete_file(file_path: str = "") -> None:
    """
    Delete a file or folder.

    Args:
        file_path (str): The path of the file or folder to delete.
    """
    file_to_rem = pathlib.Path(file_path, missing_ok=True)
    file_to_rem.unlink()
    logger.info(f"Delete file/folder success: {file_path}.")
