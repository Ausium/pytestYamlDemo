
import pytest
import os
import shutil

if __name__ == '__main__':

    try:
        # 删除之前的文件夹
        shutil.rmtree("outputs/reports")
        print('清除之前报告')
    except:
        raise Exception
    pytest.main([])
    # 直接生成报告html文件
    # os.system('allure generate  outputs/reports/data -o outputs/reports/report/html --clean')
    # 编译报告原文件并启动报告服务
    # os.system('allure serve outputs/reports/data -p 2008')


