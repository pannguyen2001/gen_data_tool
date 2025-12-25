import unittest
import pandas as pd
from .config import error_messages
from src.helpers import create_data_wrapper
from src.utils.cache_store import clear_all_cache, ttl_cache
from src.utils.column_setup import CommonColumns
from src.create_data.create_role import create_role


class TestCreateRole(unittest.TestCase):

    def test_create_role_result(self):
        """Test create role sucessfully."""
        result: dict = create_role()
        assert result["result"] == "success"
        assert result["file"] == create_role.__name__
    
    def test_create_role_common_data(self):
        """Test create common data successfully."""
        result: dict = create_role()
        data: pd.DataFrame = ttl_cache.get(create_role.__name__)
        result_columns = data.columns

        assert CommonColumns._ID.value in result_columns, error_messages["not_in_result"].safe_substitute(value=CommonColumns._ID.value)
        assert CommonColumns.CREATED_ON.value in result_columns, error_messages["not_in_result"].safe_substitute(value=CommonColumns.CREATED_ON.value)
        assert CommonColumns.CREATED_BY.value in result_columns, error_messages["not_in_result"].safe_substitute(value=CommonColumns.CREATED_BY.value)
        assert CommonColumns.MODIFIED_BY.value in result_columns, error_messages["not_in_result"].safe_substitute(value=CommonColumns.MODIFIED_BY.value)
        assert CommonColumns.MODIFIED_ON.value in result_columns, error_messages["not_in_result"].safe_substitute(value=CommonColumns.MODIFIED_ON.value)

    def test_role_in_result(self):
        """Test role in result."""
        result: dict = create_role()
        data: pd.DataFrame = ttl_cache.get(create_role.__name__)
        role_list: list = data["name"].to_list()

        assert "admin" in role_list, error_messages["not_in_result"].safe_substitute(value="admin")
        assert "teacher" in role_list, error_messages["not_in_result"].safe_substitute(value="teacher")
        assert "student" in role_list, error_messages["not_in_result"].safe_substitute(value="student")

    def tearDown(self):
        clear_all_cache()