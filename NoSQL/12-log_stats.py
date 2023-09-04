#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_co = client.logs.nginx
    
    print("{} logs\n\
          Methods:".format(nginx_co.count()))
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    logs_dict = {}
    for method in methods:
        logs_dict[method] = nginx_co.count({ "method": method })

    for method, logs in logs_dict.items():
        print("\tmethod {}: {}".format(method, logs))
