import time
import os
from datetime import datetime
import pytest
from _pytest import terminal
from utils.get_path import execute_result_dir
from utils.send_email import send_case_result_email
from utils.get_path import report_dir

 
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    # 统计总共用例数以及成功失败用例数
    total = terminalreporter._numcollected
    #用例 when='call'阶段执行成功，代表用例是成功的，teardown(前置条件) 阶段失败或者错误，不影响执行结果。
    passed = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    failed = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    error = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    skipped = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    successful = len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100
    # terminalreporter._sessionstarttime 会话开始时间
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times: %.2f' % duration, 'seconds')
    path = os.path.join(execute_result_dir,"execute_result")
    # 将用例执行结果写入txt文件中;
    with open(path, "w",encoding="utf-8") as fp:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S")
        fp.write("用例执行结果如下:\n")
        fp.write("Total: %s;\n" % total)
        fp.write("Passed: %s;\n" % passed)
        fp.write("Failed: %s;\n" % failed)
        fp.write("Errored: %s;\n" % error)
        fp.write("Skiped: %s;\n" % skipped)
        fp.write("Successful_rate: %.2f%%;\n" % successful)
        fp.write("Running_time: %s;\n" % now_time)
        fp.write("Totla_time: %.2f s;\n" % duration)
    subject = '自动化用例执行结果'
    res = f"""
    <h1>自动化用例执行结果如下:</h1>
    <div style="font-weight: bold; font-size:14px;">
        <p>Total: {total};</p>
        <p>Passed: {passed};</p>
        <p>Failed: {failed};</p>
        <p>Errored: {error};</p>
        <p>Skiped: {skipped};</p>
        <p>Successful_rate: {successful}%;</p>
        <p>Running_time: {now_time};</p>
        <p>Totla_time: {duration}s;</p>
        <a href='http://192.168.20.248:2008/index.html'>测试报告</a>
    </div>
    """
    # report_path = os.path.join(report_dir, "report.html")
    # send_case_result_email.send_email(subject,res)
