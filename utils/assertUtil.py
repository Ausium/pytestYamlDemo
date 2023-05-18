import os
import sys
sys.path.append(os.getcwd())

import ast
import jsonpath
import pymysql
from utils.logger import logger
from decimal import Decimal
from utils.extract_data import FAILED_CASE_LIST

class RespondAssert():

    def assert_response_value(self,check_list, response_data,case_data):
        """
        :param check_list: 从yaml当中，读取出来的断言列。
        :param response_data: 接口请求之后的响应数据，是字典类型。
        :case_data  用例数据
        :return: None
        """
        # 所有断言的比对结果列表
        check_res = []

        for check in check_list:
            
            # 通过jsonpath表达式，从响应结果当中拿到了实际结果
            actual = jsonpath.jsonpath(response_data.json(), check["expr"])
            if isinstance(actual, list):
                actual = actual[0]
            # 与实际结果做比对
            if check["assert_type"] == "equals_assert":
                logger.info("开始断言预期结果与实际结果是否相等。")
                check_res.append(actual == check["expected"])
            #包含断言
            elif check["assert_type"] == "contains_assert":
                logger.info("开始断言实际结果是否包含预期结果。")
                check_res.append(actual == check["expected"])
            
        if False in check_res:
            
            logger.info("用例断言结果列表:{}".format(check_res))
            logger.error("用例断言失败！")
            
            raise AssertionError
        else:
            failed_case = []
            failed_case.append(case_data['case_title'])
            failed_case.append(case_data['url'])
            failed_case.append(response_data.status_code)
            failed_case.append(response_data.json())
            FAILED_CASE_LIST.append(failed_case)
            failed_case = []
            logger.info("断言结果列表:{}".format(check_res))
            logger.info("用例断言成功！")
            
            return True

respond_assert = RespondAssert()

if __name__ == '__main__':

    check_list = [{"expr":"$.status","expected":1,"type":"assert_result"},{"expr":"$.statuss","expected":10,"type":"assert_result"}]
    response_data = {'status': 1,'statuss':10}
    res = RespondAssert().assert_response_value(check_list,response_data)
    print(res)

