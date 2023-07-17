#!/usr/bin/env python3
"""
change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    function that changes all topic
    of school document basrd on name
    """
    return mongo_collection.update_many({"name": name,
                                         {"$set": {"topics": topics}})
