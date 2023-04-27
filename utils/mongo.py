import pymongo

# conn = mongo_client('mongodb://admin:Root123@10.10.10.16:27017/?authSource=admin')

def test():

    client = pymongo.MongoClient('mongodb://admin:Root123@10.10.10.16:27017')
    print("=============")

    print(client.list_database_names())
    # 连接数据库
    # db = client.platform_admin
    # # 连接到users集合
    # users= db["area"]
    
    # print(db.list_collection_names()) # 获取数据库中所有集合名称
    # print(users.count()) # 统计users集合的文档数
 

if __name__ == '__main__':
    test()