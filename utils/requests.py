import os
import requests
import pytest
import allure
from requests.adapters import HTTPAdapter
from utils.myConf import MyConf
from utils.get_path import conf_dir
from utils.extract_data import extract_data
from utils.logger import logger

class MyRequests():

    #初始化方法
    def __init__(self):

        #请求头
        self.headers = {"Content-type": "application/json"} 
        #读取配置文件中的server
        self.base_url = MyConf(os.path.join(conf_dir,"conf.ini")).get("server","host")

    def send_requests(self,api_url,method,data):
        #处理请求头
        self.__deal_header()
        #处理请求url
        self.__deal_url(api_url)
        """
        为Session()对象设置重试次数和适配器
        max_retries参数表示最大重试次数，如果请求失败，则会自动重试指定的次数。
        sess.keep_alive = False的作用是关闭多余的连接
        """
        sess = requests.Session()
        sess.mount('http://', HTTPAdapter(max_retries=3)) 
        sess.mount('https://', HTTPAdapter(max_retries=3))     
        sess.keep_alive = False

        try:
            if method.upper() == "GET":
                logger.info("开始请求{}接口".format(api_url))
                resp = requests.request(method,self.url,params=data,headers=self.headers,verify=False)
                logger.info("接口请求成功")
                resp.close()   #关闭，确保不要过多的链接
            else: 
                logger.info("开始请求{}接口".format(api_url))
                resp = requests.request(method,self.url,json=data,headers=self.headers)
                logger.info("接口请求成功")
                resp.close()
            return resp
        except requests.exceptions.RequestException as e:
            logger.error("请求失败，错误信息为{}".format(str(e)))
            raise e

    def __deal_header(self):
        if hasattr(extract_data,"access_token"):
            self.headers["Authorization"] = "Bearer {}".format(extract_data.access_token)

    def __deal_url(self,api_url):
        url = self.base_url + api_url
        # allure.step('请求地址为：{}'.format(url))
        self.url = url
    @classmethod
    def request_log(cls):
        pass
mq = MyRequests()

if __name__ == '__main__':
    mr = MyRequests()
    url = "api/v1/pub/login/3rd"
    req_data = {"ID": "chenzanxu","secret": "25d55ad283aa400af464c76d713c07ad", "type": "default"}
    method = "post"
    reps = mr.send_requests(url,method,req_data)
    print(reps.json())