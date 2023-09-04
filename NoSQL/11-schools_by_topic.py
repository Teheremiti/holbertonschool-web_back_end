#!/usr/bin/env python3
"""Find a school based on a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having the topic"""
    return mongo_collection.find({ "topics": topic })
