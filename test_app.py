import pytest
from calculator import Calculator
from user_manager import UserManager
from data_processor import DataProcessor

def test_calculator():
    assert Calculator.add(2, 3) == 5
    assert Calculator.subtract(5, 2) == 3

def test_user_manager():
    um = UserManager()
    assert um.register_user("testuser", "test@example.com") is True

def test_data_processor():
    dp = DataProcessor()
    assert dp.clean_data(["  hello ", ""]) == ["hello"]