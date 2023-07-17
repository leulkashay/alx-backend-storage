#!/usr/bin/env python3
"""
Inserts a document
"""


def insert_school(mongo_collection, **kwargs):
    """ 
    function that inserts a new document in collection based kwargs
    """
    doc_col = mongo_collection.insert_one(kwargs)
    return doc_col.inserted_id
