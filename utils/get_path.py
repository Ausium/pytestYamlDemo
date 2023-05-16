
import os

# 1、basedir
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件路径
conf_dir = os.path.join(basedir, "config")

# 测试用例数据路径
testdata_dir = os.path.join(basedir, "testdata")

# 日志路径
log_dir = os.path.join(basedir, "outputs", "logs")

# 报告路径
report_dir = os.path.join(basedir, "outputs", "report")

#用例执行结果路径
execute_result_dir = os.path.join(basedir, "outputs", "execute_result")

if __name__ == "__main__" :
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(basedir)


