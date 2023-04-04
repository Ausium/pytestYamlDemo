from asyncio.log import logger
import pytest
from utils.extract_data import Data
from utils.requests import MyRequests


@pytest.fixture(scope="session",autouse=True)
def global_init():
    """
    前置操作,初始化数据
    1、从Data里拿出来用户数据
    2、调用sql从数据库查询,如果不存在则注册
    """
    pass