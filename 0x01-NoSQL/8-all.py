#!/usr/bin/env python3
"""
List all documents in python module
"""


def list_all(mongo_collection):
    """ lists all documents """
    return mongo_collection.find()
