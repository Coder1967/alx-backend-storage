#!/usr/bin/env python3

"""
module for the 10th task
"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a new document
    in a collection based on kwargs
    """

    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
