#!/usr/bin/env python3
"""
stats about Nginx logs
"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')

    nginx_collection = client.logs.nginx

    print("{} logs".format(nginx_collection.count_documents({})))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))


    count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(count))


    top10_ips = nginx_collection.aggregate([
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}
        }},

        {"$sort": {"count": -1}},
        {"$limit": 10},

        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")

    for top_ip in top10_ips:
        ip = top_ip.get('ip')
        count = top_ip.get('count')
        print("\t{}: {}".format(ip, count))
