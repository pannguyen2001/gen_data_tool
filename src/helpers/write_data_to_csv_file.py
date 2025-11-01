import pandas as pd
from loguru import logger

@logger.catch
def write_data_to_csv_file(data: pd.DataFrame|dict = None, file_name: str = ""):
    """
    Write data to a CSV file.

    Args:
        data (pd.DataFrame|dict, optional): The data to write to the CSV file. Defaults to None.
        file_name (str, optional): The name of the CSV file to write to.

    Returns:
        None
    """

    if data is None:
        raise ValueError("Data is None")
    if file_name == "":
        raise ValueError("File name is empty")

    if not isinstance(data, pd.DataFrame) and not isinstance(data, dict):
        raise ValueError("Data is not a DataFrame or dict")
    if not isinstance(file_name, str):
        raise ValueError("File name is not a string")

    if not file_name.endswith('.csv'):
        raise ValueError("File name does not end with .csv")

    if isinstance(data, pd.DataFrame):
        data.to_csv(file_name, index=False, encoding='utf-8')
    elif isinstance(data, dict):
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            for key, value in data.items():
                file.write(str(key) + ',' + str(value) + '\n')