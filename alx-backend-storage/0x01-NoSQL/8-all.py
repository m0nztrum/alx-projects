#!/usr/bin/env python3
"""
Task 8
"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    return [docs for docs in mongo_collection.find()]
