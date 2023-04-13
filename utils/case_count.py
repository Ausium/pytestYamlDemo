import time
import os
from datetime import datetime
import pytest
from _pytest import terminal
from utils.get_path import execute_result_dir

class CaseCountName():
    ERROR: str = "error_count"
    FAILED: str = "failed_count"
    PASSED: str = "passed_count"
    SKIPPED: str = "skip_count"
    TOTAL: str = "total_count"
    SUCCESSFUL: str = "successful"

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    # 统计总共用例数以及成功失败用例数
    CaseCountName.TOTAL = terminalreporter._numcollected
    #用例 when='call'阶段执行成功，代表用例是成功的，teardown(前置条件) 阶段失败或者错误，不影响执行结果。
    CaseCountName.PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    CaseCountName.FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    CaseCountName.ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    CaseCountName.SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    CaseCountName.SUCCESSFUL = len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100
    # terminalreporter._sessionstarttime 会话开始时间
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times: %.2f' % duration, 'seconds')
    path = os.path.join(execute_result_dir,"execute_result")
    # 写入result.txt文件中；
    with open(path, "w",encoding="utf-8") as fp:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S")
        fp.write("用例执行结果如下:\n")
        fp.write("Total: %s;\n" % CaseCountName.TOTAL)
        fp.write("Passed: %s;\n" % CaseCountName.PASSED)
        fp.write("Failed: %s;\n" % CaseCountName.FAILED)
        fp.write("Errored: %s;\n" % CaseCountName.ERROR)
        fp.write("Skiped: %s;\n" % CaseCountName.SKIPPED)
        fp.write("Successful_rate: %.2f%%;\n" % CaseCountName.SUCCESSFUL)
        fp.write("Running_time: %s;\n" % now_time)
        fp.write("Totla_time: %.2f s;\n" % duration)