import os
import sys
sys.path.append(os.getcwd())

import re
import jsonpath
from utils.extract_data import extract_data,ExtractData
from utils.logger import logger
from utils.function import *

def replace_case(case_data):
    #yaml文件中的函数处理
    case_dict = replace_func(case_data)
    
    case_str = str(case_dict)
    regex = r'\${(.*?)}'
    to_be_replace_marks_list = re.findall(regex,case_str)
    print(to_be_replace_marks_list)
    logger.info("提取的用例标识符:{}".format(to_be_replace_marks_list))
    
    if to_be_replace_marks_list:
        for mark in to_be_replace_marks_list:
            if hasattr(extract_data, mark):
                # 使用全局变量Data类的mark属性值，去替换测试用例当中的${mark}
                case_str = case_str.replace(f"${mark}", getattr(extract_data,mark))
                logger.info("替换用例标识符,标识符值为:{}:{}".format(mark,setattr(extract_data,mark)))

    #将完全替换后的一整个测试用例，转换回字典
    new_case_data = eval(case_str)
    return new_case_data

def replace_func(data):
    """
    data: 读取出的yaml用例
    函数用来处理yaml文件中的函数
    """
    if isinstance(data, dict):
        return {k: replace_func(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_func(item) for item in data]
    elif isinstance(data, str) and "random" in data:
        return data.replace(data, str(eval(str(data))))
    else:
        return data

def extract_data_from_response(extract_epr, response_dict):
    """
    从响应结果当中提取值，并设置为Data类的属性。
    :param extract_epr: excel当中extract列中的提取表达式。是一个字典形式的字符串。
                        key为全局变量名。value为jsonpath提取表达式。
                        '{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
    :param response: http请求之后的响应结果。字典类型。
    :return:None
    """
    # 1、遍历1中字典的key,value.key是全局变量名，value是jsonpath表达式。
    for key,value in extract_epr.items():
        result = jsonpath.jsonpath(response_dict, value)
        #如果提取到了真正的值，那么将它设置为Data类的属性。key是全局变量名，result[0]就是提取后的值,jsonpath找了就是列表，所以就取第一个，找不到返回False
        if result:
            setattr(ExtractData, key, str(result[0]))

if __name__ == '__main__':
    case_str = {'id': 1, 'type': 'setup', 'title': random_number(10),'phone':'${phone}','phone':'${phone}'}
    res = replace_case(case_str)
    print(res)
    # print(res)
    # print(dir(extract_data))
#     resp = {
#     "data": {
#         "access_token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODMzNDI3OTEsImlhdCI6MTY4MDc1MDc5MSwibmJmIjoxNjgwNzUwNzkxLCJzdWIiOiJvd0hfSndJVGJmQ1VNUXVyMlQ2SEVlSTRZMl9BOjE4MTQ1ODQ1ODIwOmZhbHNlIn0.UYWzQKEptwE-HcNinOwmRXRSDDLR2GLtWM0HraIrMyQ3Tov8C-XRcFVoeW2HPoBOKh92AGDjH4h97hmd2dC70A",
#         "token_type": "Bearer",
#         "expires_at": 1683342791,
#         "phone": "18145845820"
#     },
#     "status": 1
# }
#     cases = {"access_token": "$.data.access_token"}
#     extract_data_from_response(cases,resp)




