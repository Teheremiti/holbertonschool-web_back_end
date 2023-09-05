#!/usr/bin/env python3
"""Method top_students that lists all students in a dict
sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    avg_scores = {}
    for student in mongo_collection.find():
        total = 0
        number_of_topics = 0
        for topic in student['topics']:
            total += student['topics'].get('score')
            number_of_topics += 1
        avg_scores[student['name']] = total / number_of_topics
    
    return dict(sorted(avg_scores.items(), key = lambda item: item[1],
                       reverse=True))
