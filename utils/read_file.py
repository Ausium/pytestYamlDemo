import os
import sys
sys.path.append(os.getcwd())

from pathlib import Path
import requests
import yaml
from utils.get_path import testdata_dir
from config.config import exclude_file, exclude_dir, Environment
from utils.logger import logger


class ReadFile():
    
    project_directory = str(Path(__file__).parent.parent) + '/'
    # 读取
    @classmethod
    def get_test_data(cls,test_data_path):
        case = []  # 存储测试用例名称
        http = []  # 存储请求对象
        expected = []  # 存储预期结果
        with open(test_data_path,'r', encoding='utf-8') as f:
            dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
            test = dat['tests']
            for td in test:
                case.append(td.get('case', ''))
                http.append(td.get('http', {}))
                expected.append(td.get('expected', {}))
        parameters = zip(case, http, expected)
        return case, parameters

    @classmethod
    def case_file_location(cls, case_title):
        '''
        :param case_name: 用例名称
        :return: 判断这个用例名称是不是在哪一个文件里面（前提用例名称唯一），返回文件名（含路径）
        '''
        path_list = cls.file_execute_list()
        for i in path_list:
            if case_title in cls.read_yaml(i).keys():
                return i

    @classmethod
    def file_execute_list(cls, exclude_file=exclude_file, exclude_dir=exclude_dir):
        '''
        :param exclude_dir: 要排除的目录（二级目录）例子：ctms  list格式
        :param exclude_file: 要排除的文件（case目录下所有文件）例子：case/ctms/ctms_main.yaml   case/waybill.yaml list格式
        :return: 获取case下的所有用例文件列表,最多支持二级目录,通用排除文件返回最终要执行的用例文件
        '''
        file_list = []
        # case_path = cls.project_directory + 'testdata'
        case_path = testdata_dir
        for filename in os.listdir(case_path):
            if 'yaml' in filename:
                file_list.append('case/' + filename)
            else:
                for i in os.listdir(case_path + '/' + filename):
                    if filename in exclude_dir:
                        continue
                    if 'yaml' in i:
                        file_list.append('testdata/' + filename + '/' + i)
        if exclude_file != []:
            for i in exclude_file:
                file_list.remove(i)
        
        return file_list

    @classmethod
    def read_yaml(cls, path):
        '''读取yaml文件,以字典格式返回{'用例标题':{'path':'/test','data':{'id':1}}}'''
        path = cls.project_directory + path
        with open(path, 'r', encoding='utf-8') as f:
                content = yaml.load(f.read(), Loader=yaml.Loader)
                return content

    @classmethod
    def read_case(cls):
        '''读取case下需要执行的用例文件并返回用例数据'''
        path_list = cls.file_execute_list()
        logger.info("执行的用例文件为:{}".format(path_list))
        case_data = {}
        for i in path_list:
            case_data.update(cls.read_yaml(i)) 
        for case_key, case_value in case_data.items():
            if case_value["is_run"] == True:
                case_value["case_title"] = case_key
            yield case_value                


if __name__ == "__main__" :
    _read_name = ReadFile()
    print(ReadFile.read_case())
    
    

    
    