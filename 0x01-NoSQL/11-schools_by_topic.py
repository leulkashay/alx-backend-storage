#!/usr/bin/env python3
"""
learn python module
"""


def schools_by_topic(mongo_collection,  topic):
    """
    function that retuns all the list school
    having a specific topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
