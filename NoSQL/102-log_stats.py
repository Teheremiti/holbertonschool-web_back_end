#!/usr/bin/env python3
"""Improved python script that provides some stats about Nginx logs
stored in MongoDB and the Top IPs"""

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_logs_per_method(mongo_co):
    """Returns a dict with all methods with their log count"""
    logs_per_method = {}
    for method in METHODS:
        logs_per_method[method] = mongo_co.count_documents({"method": method})
    return logs_per_method


def print_status_checks(mongo_co):
    """Prints the total number of status checks to stdout"""
    status_checks = nginx_co.count_documents({"method": "GET",
                                              "path": "/status"})
    print("{} status check".format(status_checks))


def get_logs_per_ip(mongo_co):
    """Returns a list of dicts with the Top 10 IPs with the most logs"""
    logs_per_ip = mongo_co.aggregate([
        {'$group': {'IP': '$ip', 'logs': {'$sum': 1}}},
        {'$sort': {'logs': -1}},
        {'$limit': 10}
    ])
    return logs_per_ip


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_co = client.logs.nginx

    print("{} logs\nMethods:".format(nginx_co.count_documents({})))

    logs_per_method = get_logs_per_method(nginx_co)
    for method, logs in logs_per_method.items():
        print("\tmethod {}: {}".format(method, logs))

    print_status_checks(nginx_co)

    print("IPs:")
    logs_per_ip = get_logs_per_ip(nginx_co)
    for ip_logs in logs_per_ip:
        print("\t{}: {}".format(ip_logs.get('IP'), ip_logs.get('logs')))
