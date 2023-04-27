import os
import sys
sys.path.append(os.getcwd())

import ast
import jsonpath
import pymysql
from utils.logger import logger
from decimal import Decimal



class RespondAssert():

    def assert_response_value(self,check_list, response_dict):
        """
        :param check_list: 从yaml当中，读取出来的断言列。
        :param response_dict: 接口请求之后的响应数据，是字典类型。
        :return: None
        """
        # 所有断言的比对结果列表
        check_res = []

        for check in check_list:
            
            # 通过jsonpath表达式，从响应结果当中拿到了实际结果
            actual = jsonpath.jsonpath(response_dict, check["expr"])
            if isinstance(actual, list):
                actual = actual[0]
            # 与实际结果做比对
            if check["assert_type"] == "equals_assert":
                logger.info("比对2个值是否相等。")
                logger.info("比对结果为：{}".format(actual == check["expected"]))
                check_res.append(actual == check["expected"])
            #包含断言
            elif check["assert_type"] == "contains_assert":
                logger.info("比对2个值的大小。")
                logger.info("比对结果为：{}".format(actual > check["expected"]))
            #结果断言
            elif check["assert_type"] == "assert_result":
                logger.info("比对2个值是否相等。")
                logger.info("比对结果为：{}".format(actual == check["expected"]))
                check_res.append(actual == check["expected"])
            
        if False in check_res:
            logger.error("断言失败！")
            logger.info("断言结果列表:{}".format(check_res))
            raise AssertionError
        else:
            logger.info("断言结果列表:{}".format(check_res))
            logger.info("所有断言成功！")
            return True
respond_assert = RespondAssert()

if __name__ == '__main__':

    check_list = [{"expr":"$.status","expected":1,"type":"assert_result"},{"expr":"$.statuss","expected":10,"type":"assert_result"}]
    response_dict = {'status': 1,'statuss':10}
    res = RespondAssert().assert_response_value(check_list,response_dict)
    print(res)

