#!/usr/bin/env python3
"""Write a Python function that changes all topics
of a school document based on the name:
* Prototype: def update_topics(mongo_collection, name, topics):
* mongo_collection will be the pymongo collection object
* name (string) will be the school name to update
* topics (list of strings) will be the list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """list of topics approached in the school"""
    new_topics = mongo_collection.update_many({"name": name},
                                              {'$set': {"topics": topics}})
    return new_topics
