from pymongo import mongo_client

conn = mongo_client('mongodb://admin:Root123@10.10.10.16:27017/?authSource=admin')