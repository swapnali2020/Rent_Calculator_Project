import pytest
from Framework_RentCalculator_Project.src.app_logic import *
from Framework_RentCalculator_Project.test_data.test_data_file import *

@ pytest.fixture(scope="function")
def cal_setup():
    obj = AppFunction(browser,url,wait_time)
    return obj