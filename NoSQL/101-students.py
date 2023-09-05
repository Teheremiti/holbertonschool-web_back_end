#!/usr/bin/env python3
"""Method top_students that lists all students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    for student in mongo_collection.find():
        total = 0
        number_of_topics = 0
        for topic in student['topics']:
            total += topic['score']
            number_of_topics += 1
        student['averageScore'] = total / number_of_topics
    
    return sorted(mongo_collection, key = lambda item: item[2], reverse=True)
