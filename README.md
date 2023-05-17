# ApiAuto

本项目实现接口自动化的技术选型：**Python+Requests+Pytest+YAML+pytest-html** 
## 项目说明

本项目在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。

首先利用Python把HTTP接口封装成Python接口，测试数据则通过YAML文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合pytest-html输出测试报告。

后续再对接口自动化进行Jenkins持续集成。

## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```

接着，修改 ```config/setting.ini``` 配置文件，在Windows环境下，安装相应依赖之后，在命令行窗口执行命令：


## 项目结构

- api ====>> 接口封装层，如封装HTTP接口为Python接口
- utils ====>> 各种工具类
- config ====>> 配置文件
- testdata ====>> 测试数据文件管理
- pytest.ini ====>> pytest配置文件
- requirements.txt ====>> 相关依赖包文件
