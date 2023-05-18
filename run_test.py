
import pytest
import os
import shutil
from utils.logger import logger

if __name__ == '__main__':
    if os.path.exists("outputs/report"):
        try:
            # 删除之前的文件夹
            shutil.rmtree("outputs/report")
            print('清除之前报告')
        except:
            raise Exception
    else:
        print("文件夹不存在")
   
    # pytest.main([])
    # 直接生成报告html文件
    os.system('pytest --html=./outputs/report/report.html --self-contained-html')
    # os.system('allure generate  outputs/reports/data -o outputs/reports/report/html --clean')
    # # 编译报告原文件并启动报告服务
    # os.system('allure serve outputs/reports/data -p 2008')


