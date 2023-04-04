import os
import sys
sys.path.append(os.getcwd())

import pytest
import allure
from utils.requests import mq
from utils.allure_ import allure_title,allure_step_no
from utils import logger
from utils.read_file import ReadFile
from utils.get_path import testdata_dir
from utils.requests import mq


# path = os.path.join(testdata_dir,"login","login.yaml")
# case,parameters = ReadFile.get_test_data(path)
# list_params=list(parameters)


@pytest.mark.parametrize("case_data",ReadFile.read_case())
def test_main(case_data):
    print("case_data is {}".format(case_data))
    mq.send_requests(case_data["url"],case_data["method"],case_data["data"])
    # logger.info("")
    case_file_location = ReadFile.case_file_location(case_data['case_title'])
    print("该用例属于{}文件".format(case_file_location))
    allure_title(case_data['case_title'])
    # print("========================")
    # resp = mq.send_requests(data[0][1]["path"],data[0][1]["method"],data[0][1]["data"])
    # print(resp.json())



