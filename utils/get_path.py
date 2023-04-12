
import os

# 1、basedir
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼到配置文件路径
conf_dir = os.path.join(basedir, "config")

# 拼接  测试数据路径
testdata_dir = os.path.join(basedir, "testdata")

# 日志路径
log_dir = os.path.join(basedir, "outputs", "logs")

# 报告路径
report_dir = os.path.join(basedir, "outputs", "reports")

#用例执行结果路径
execute_result_dir = os.path.join(basedir, "outputs", "execute_result")

if __name__ == "__main__" :
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf_dir = os.path.join(basedir, "config")
    print(conf_dir)



# # 1、basedir
# basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# def get_confPath():
#     # 拼到配置文件路径
#     conf_dir = os.path.join(basedir, "Conf")
#     return conf_dir

# # 拼接  测试数据路径
# def get_testDataPath():
#     testdata_dir = os.path.join(basedir, "Excle_test")
#     return testdata_dir

# # 日志路径
# def get_logPath():
#     log_dir = os.path.join(basedir, "outputs", "logs")
#     return log_dir

# # 报告路径
# def get_logPath():
#     report_dir = os.path.join(basedir, "outputs", "reports")
#     return report_dir