#!/usr/bin/env python3

"""
module for the eleventh task
"""


def update_topics(mongo_collection, name, topics):
    """
    updates a document in the mongo db
    """

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
