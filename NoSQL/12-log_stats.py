#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs using MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    ngix_collection = client.logs.nginx

    logs = ngix_collection.count_documents({})
    print("{} logs".format(logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = ngix_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    count = ngix_collection.count_documents({"method": "GET",
                                            "path": "/status"})
    print(f"{count} status check")
