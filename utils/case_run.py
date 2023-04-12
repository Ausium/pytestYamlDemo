from utils.requests import mq
from utils.replace import replace_case, extract_data_from_response
from utils.extract_data import extract_data

def case_run(case_data):

    replace_case_data = replace_case(case_data)

    response_data = mq.send_requests(replace_case_data["url"],replace_case_data["method"],replace_case_data["data"])
    # print("response_data is {}".format(response_data.json()))
    if replace_case_data["extract_key"]:
        extract_data_from_response(replace_case_data["extract_key"],response_data.json())
    print(dir(extract_data))
    if hasattr(extract_data,"access_token"):
        print(extract_data.access_token)
    else:
        print("==================该属性不存在==============")


    


