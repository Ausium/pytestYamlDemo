import os
import requests
import pytest
import allure
from utils.myConf import MyConf
from utils.get_path import conf_dir
from utils.extract_data import extract_data

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
        if method.upper() == "GET":
            resp = requests.request(method,self.url,params=data,headers=self.headers)
        else: 
            resp = requests.request(method,self.url,json=data,headers=self.headers)
        return resp

    def __deal_header(self):
        if hasattr(extract_data,"access_token"):
            self.headers["Authorization"] = "Bearer {}".format(extract_data.access_token)

    def __deal_url(self,api_url):
        url = self.base_url + api_url
        # allure.step('请求地址为：{}'.format(url))
        print(url)
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