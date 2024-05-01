#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Change the list of topics for documents with given name.
    """
    name = {"name": name}
    new = {"$set": {"topics": topics}}
    mongo_collection.update_many(name, new)
