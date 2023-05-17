import time
import os
from datetime import datetime
import pytest
from _pytest import terminal
from utils.get_path import execute_result_dir
from utils.send_email import send_case_result_email
from utils.get_path import report_dir
from utils.make_html_table import make_html_table
from utils.extract_data import FAILED_CASE_LIST,TEST_RESULT



def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    # 统计总共用例数以及成功失败用例数
    total = terminalreporter._numcollected
    #用例 when='call'阶段执行成功，代表用例是成功的，teardown(前置条件) 阶段失败或者错误，不影响执行结果。
    passed = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    failed = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    successful = len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100
    # terminalreporter._sessionstarttime 会话开始时间
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    duration = time.time() - terminalreporter._sessionstarttime
    case_execute_result = []
    case_execute_result.append(now_time)
    case_execute_result.append(total)
    case_execute_result.append(passed)
    case_execute_result.append(failed)
    case_execute_result.append(successful)
    case_execute_result.append(duration)
    TEST_RESULT.append(case_execute_result)

    path = os.path.join(execute_result_dir,"execute_result")
    # 将用例执行结果写入txt文件中;
    with open(path, "w",encoding="utf-8") as fp:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S")
        fp.write("用例执行结果如下:\n")
        fp.write("Total: %s;\n" % total)
        fp.write("Passed: %s;\n" % passed)
        fp.write("Failed: %s;\n" % failed)
        fp.write("Successful_rate: %.2f%%;\n" % successful)
        fp.write("Running_time: %s;\n" % now_time)
        fp.write("Totla_time: %.2f s;\n" % duration)
    subject = '自动化用例执行结果'
    _html_table = '<h2>自动化用例执行结果</h2>'
    _html_table += """
<table border="1" bordercolor="#c8c9cc"; cellpadding="7" cellspacing="0"; style="table-layout: fixed; font-size:14px;width: 1200px;border-collapse: collapse;" >
  <tr>
    <td style="padding: 10px; background-color: #f2f2f2; border: 1px solid #ccc;text-align:center; overflow: hidden;width: 10%;">Cell 1</td>
    <td style="padding: 10px; background-color: #f2f2f2; border: 1px solid #ccc;text-align:center; overflow: hidden;width: 10%;">Cell 2</td>
    <td style="padding: 10px; background-color: #f2f2f2; border: 1px solid #ccc;text-align:center; overflow: hidden;width: 10%;">Cell 3</td>
    <td style="padding: 10px; background-color: #f2f2f2; border: 1px solid #ccc;text-align:center; overflow: hidden;width: 10%;">Cell 4</td>
    <td style="padding: 10px; background-color: #f2f2f2; border: 1px solid #ccc;text-align:center; overflow: hidden;width: 10%;">Cell 5</td>
    <td style="padding: 10px; background-color: #f2f2f2; border: 1px solid #ccc;text-align:center; overflow: hidden;width: 10%;">Cell 6</td>
    <td style="padding: 10px; background-color: #f2f2f2; border: 1px solid #ccc;text-align:center; overflow: hidden;width: 40%;">Cell 7</td>
  </tr>
  <tr>
    <td style="padding: 10px; background-color: #fff; border: 1px solid #ccc;">Cell 3</td>
    <td style="padding: 10px; background-color: #fff; border: 1px solid #ccc;">Cell 4</td>
    <td style="padding: 10px; background-color: #fff; border: 1px solid #ccc;">Cell 5</td>
    <td style="padding: 10px; background-color: #fff; border: 1px solid #ccc;">Cell 6</td>
    <td style="padding: 10px; background-color: #fff; border: 1px solid #ccc;">Cell 7</td>
    <td style="padding: 10px; background-color: #fff; border: 1px solid #ccc;">Cell 8</td>
    <td style="padding: 10px; background-color: #fff; border: 1px solid #ccc;word-break: break-all;">Cell 9 'data': {'access_token':'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9eyJleHAiOjE2ODYwMzIyNTQsImlhdCI6MTY4NDIxNzg1NCwibmJmIjoxNjg0MjE3ODU0LCJzdWIiOiJhNzk3YmVhNS01N2JkLTRkZDctYjEwYS05YTM4YjM5MmY5OGQ6Y2hlbnphbnh1OnRydWUifQiUSYgBQTMbUi49nBrQDHmTKbXhRBF39TyzRr3r9Veb7CEQwV4qIdorma0x3iwWvxoWOkV5RjDwGhiiNknOUtuQ', 'token_type': 'Bearer'</td>
  </tr>
</table>
    """
    table_title = '1、用例执行结果统计'
    table_content = TEST_RESULT
    table_header = ['用例执行开始时间','用例执行总数','执行成功数量','执行失败数量','用例成功率','执行用例总时']
    # _html_table += make_html_table(table_title,table_header,table_content)


    table_title = '2、用例执行结果统计'
    table_content = FAILED_CASE_LIST
    table_header = ['接口名称','接口地址','http_code','接口响应结果']
    # _html_table += make_html_table(table_title,table_header,table_content)
    report_path = os.path.join(report_dir, "report.html")
    send_case_result_email.send_email(subject,_html_table,report_path)
