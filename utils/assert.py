
import ast
import jsonpath
from utils.logger import logger
from decimal import Decimal


class MyAssert:

    def assert_response_value(self,check_str, response_dict):
        """
        :param check_str: 从excel当中，读取出来的断言列。是一个列表形式的字符串。里面的成员是一个断言
        :param response_dict: 接口请求之后的响应数据，是字典类型。
        :return: None
        """
        # 所有断言的比对结果列表
        check_res = []

        # 把字符串转换成python列表
        check_list = eval(check_str)  # 比eval安全一点。转成列表。

        for check in check_list:
            logger.info("要断言的内容为：\n{}".format(check))
            # 通过jsonpath表达式，从响应结果当中拿到了实际结果
            actual = jsonpath.jsonpath(response_dict, check["expr"])
            if isinstance(actual, list):
                actual = actual[0]
            logger.info("从响应结果当中，提取到的值为:\n{}".format(actual))
            logger.info("期望结果为:\n{}".format(check["expected"]))
            # 与实际结果做比对
            if check["type"] == "==":
                logger.info("比对2个值是否相等。")
                logger.info("比对结果为：\n{}".format(actual == check["expected"]))
                check_res.append(actual == check["expected"])
            elif check["type"] == "gt":
                logger.info("比对2个值的大小。")
                logger.info("比对结果为：\n{}".format(actual > check["expected"]))

        if False in check_res:
            logger.error("部分断言失败！，请查看比对结果为False的")
            raise AssertionError
            # return False
        else:
            logger.info("所有断言成功！")
            return True

if __name__ == '__main__':
    # 已经从excel当中读取出来的字符串
    check_db_str = """[{"sql":"select id from member where mobile_phone='15500000000'","expected":1,"db_type":"count"}]"""
    res = MyAssert().assert_db(check_db_str)
    print(res)

