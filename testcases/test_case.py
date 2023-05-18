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
from case_run.case_execute import case_execute
from utils.logger import logger


@pytest.mark.parametrize("case_data",ReadFile.read_case())
def test_main(case_data):

    case_execute(case_data)
    case_file_location = ReadFile.case_file_location(case_data['case_title'])
    logger.info("用例名称:{},该用例属于{}文件".format(case_data['case_title'],case_file_location))
    allure_title(case_data['case_title'])




