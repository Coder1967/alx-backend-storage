#!/usr/bin/env python3

"""
module for the 12th task
"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

print("{} logs".format(collection.count_documents({})))
print("Methods:")
print("\tmethod GET: {}".format(collection.count_documents({"method": "GET"})))
print("\tmethod POST: {}".format(
    collection.count_documents({"method": "POST"})))
print("\tmethod PUT: {}".format(collection.count_documents({"method": "PUT"})))
print("\tmethod PATCH: {}".format(
    collection.count_documents({"method": "PATCH"})))
print("\tmethod DELETE: {}".format(
    collection.count_documents({"method": "DELETE"})))
