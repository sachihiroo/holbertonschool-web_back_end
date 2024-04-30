#!/usr/bin/env python3
"""function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """list all the documents in a given mongo DB collection."""
    if mongo_collection is None:
        return []
    return mongo_collection.find()
