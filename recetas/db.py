import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

_client = None


def get_client():
    global _client
    if _client is None:
        uri = os.environ["MONGO_URI"]
        _client = MongoClient(uri)
    return _client


def get_database():
    return get_client()["examen"]
