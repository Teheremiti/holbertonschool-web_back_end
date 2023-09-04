#!/usr/bin/env python3
"""Insert a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Returns the _id of the new document"""
    return mongo_collection.insert_one(kwargs)
