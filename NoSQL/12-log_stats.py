#!/usr/bin/env python3
"""Write a Python script that provides some stats
about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


if __name__ == "__main__":
    """Python script that provides stats about Nginx logs"""
    client = MongoClient()
    logs_db = client.logs
    nginx_collection = logs_db.nginx
    x = nginx_collection.count_documents({})
    print(f"{x}: logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    count_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{count_status} status check")
