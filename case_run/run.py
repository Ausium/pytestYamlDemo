from utils.requests import mq
from utils.replace import replace_case, extract_data_from_response
from utils.extract_data import extract_data
from utils.assertUtil import RespondAssert
from utils.logger import logger

def case_execute(case_data):

    replace_case_data = replace_case(case_data)
    response_data = mq.send_requests(replace_case_data["url"],replace_case_data["method"],replace_case_data["data"])
    
    if replace_case_data.get("extract_key") is not None:
        extract_data_from_response(replace_case_data["extract_key"],response_data.json())
        
    if replace_case_data.get("assert_response_value") is not None:
        RespondAssert().assert_response_value(replace_case_data["assert_response_value"],response_data.json())
    else:
        logger.info("该用例不存在assert_response_value字段!")


    


