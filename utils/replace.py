import os
import sys
sys.path.append(os.getcwd())

import re
import jsonpath
from utils.extract_data import extract_data,ExtractData

def replace_case(case_dict):
    # 第一步，把整个测试用例转换成字符串
    case_str = str(case_dict)
    # 第二步，利用正则表达式提取mark标识符
    regex = r'\${(.*?)}'
    to_be_replace_marks_list = re.findall(regex,case_str)

    # 第三步：遍历标识符mark，如果标识符是全局变量Data类的属性名，则用属性值替换掉mark
    if to_be_replace_marks_list:
        for mark in to_be_replace_marks_list:
            # 如果全局变量Data类有mark这个属性名
            if hasattr(extract_data, mark):
                # logger.info("将标识符{}替换为{}".format(mark,getattr(Data,mark)))
                # 使用全局变量Data类的mark属性值，去替换测试用例当中的${mark}
                case_str = case_str.replace(f"${mark}", getattr(extract_data,mark))

    # 第四步：将完全替换后的一整个测试用例，转换回字典
    new_case_data = eval(case_str)
    return new_case_data

def extract_data_from_response(extract_epr, response_dict):
    """
    从响应结果当中提取值，并设置为Data类的属性。
    :param extract_epr: excel当中extract列中的提取表达式。是一个字典形式的字符串。
                        key为全局变量名。value为jsonpath提取表达式。
                        '{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
    :param response: http请求之后的响应结果。字典类型。
    :return:None
    """
    # 1、从excel中读取的提取表达式，转成字典对象
    # extract_dict = eval(extract_epr)
    # print(extract_dict)
    # 2、遍历1中字典的key,value.key是全局变量名，value是jsonpath表达式。
    for key,value in extract_epr.items():
        # 根据jsonpath从响应结果当中，提取真正的值。value就是jsonpath表达式
        result = jsonpath.jsonpath(response_dict, value)
        # jsonpath找了就是列表，找不到返回False
        # 如果提取到了真正的值，那么将它设置为Data类的属性。key是全局变量名，result[0]就是提取后的值,因为返回的是一个列表，所以就取第一个
        if result:
            setattr(ExtractData, key, str(result[0]))
            # ExtractData.key = result[0]
            # logger.info("提取的变量名为：{}，提取到的值为：{},并设置为Data类的属性和值。".format(key,str(result[0])))

if __name__ == '__main__':
    # case_str = {'id': 1, 'type': 'setup', 'title': '${登录}','phone':'${phone}','phone':'${phone}'}
    # res = replace_case(case_str)
    # print(res)
    print(dir(extract_data))
    
#     resp = {
#     "data": {
#         "access_token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODMzNDI3OTEsImlhdCI6MTY4MDc1MDc5MSwibmJmIjoxNjgwNzUwNzkxLCJzdWIiOiJvd0hfSndJVGJmQ1VNUXVyMlQ2SEVlSTRZMl9BOjE4MTQ1ODQ1ODIwOmZhbHNlIn0.UYWzQKEptwE-HcNinOwmRXRSDDLR2GLtWM0HraIrMyQ3Tov8C-XRcFVoeW2HPoBOKh92AGDjH4h97hmd2dC70A",
#         "token_type": "Bearer",
#         "expires_at": 1683342791,
#         "phone": "18145845820"
#     },
#     "status": 1
# }

# cases = {"access_token": "$.data.access_token"}

# extract_data_from_response(cases,resp)
    # del extract_data.access_token
    # print(dir(extract_data))
# print(extract_data.access_token)




