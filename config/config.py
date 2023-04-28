#!/usr/bin/env python
# -*- coding: utf-8 -*-


#框架测试环境配置
Environment='test_environment'
#日志这里用自己电脑的文件路径
#执行用例要排除的case下的二级目录
exclude_dir=['test','ctms']
#执行用例要排除的case下的文件
exclude_file=["car.yaml"]
#数据库配置，使用数据库操作时使用

## 钉钉方法路径，配置发送钉钉
dd_path=r'D:\python2022\pytest_api_2022.6.10\tool\dd_push.py'