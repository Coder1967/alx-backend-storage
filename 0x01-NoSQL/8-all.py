#!/usr/bin/env python3

"""
module for the 9th task
"""


def list_all(mongo_collection):
    """
    function that lists all
    documents in a collection
    """
    return ([document for document in mongo_collection.find()])
