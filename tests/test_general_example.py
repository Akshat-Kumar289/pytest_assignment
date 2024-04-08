import pytest
from unittest.mock import patch
from src.general_example import GeneralExample


@pytest.fixture
def general_example():
    return GeneralExample()


def test_flatten_dictionary(general_example):
    input_dict = {'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
    expected_output = [0, 1, 2, 3, 10, 22, 42, 55]
    assert general_example.flatten_dictionary(input_dict) == expected_output


@patch('src.general_example.GeneralExample.load_employee_rec_from_database')
def test_fetch_emp_details(mock_load_employee_rec_from_database, general_example):
    mock_load_employee_rec_from_database.return_value = ['emp001', 'Sam', '100000']
    expected_details = {'empId': 'emp001', 'empName': 'Sam', 'empSalary': '100000'}
    assert general_example.fetch_emp_details() == expected_details
