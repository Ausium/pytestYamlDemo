#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time    : 2022/6/17 
@Author  : LL
@File    : allure_.py
'''
import json

import allure

from utils.logger import logger


def allure_title(title):
    """allure中显示的用例标题"""
    allure.dynamic.title(title)

def allure_description(description):
    """allure中显示的用例描述"""
    allure.dynamic.description(description)
#
# def allure_step(step, var) :
#     if type(var)==list:
#         var=''.join(var)
#     logger.info(var)
#
#     """
#     :param step: 步骤及附件名称
#     :param var: 附件内容
#     """
#     with allure.step(step):
#         allure.attach(
#             json.dumps(
#                 var,
#                 ensure_ascii=False,
#                 indent=4),
#             step,
#             allure.attachment_type.JSON)
def allure_step_no(step: str):
    """
    无附件的操作步骤
    :param step: 步骤名称
    :return:
    """
    with allure.step(step):
        pass
