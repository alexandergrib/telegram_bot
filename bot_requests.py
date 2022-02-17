import requests
import json
import pymongo
import bson
import os
import datetime

if os.path.exists("env.py"):
    import env

MONGO_URI = env.MONGO_URI


def mongo_connect(url):
    try:
        mongo_conn = pymongo.MongoClient(url)
        # print("Mondo is connected")
        return mongo_conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# conn = mongo_connect(MONGO_URI)
# orders = conn["tele_bot"]["orders"]


def get_user_orders(username):
    conn = mongo_connect(MONGO_URI)
    conn_db = conn["tele_bot"]["orders"]
    orders = conn_db.find(
        {"$and": [{"worker_id": {"$eq": username}},
                  # {"date": {"$eq": datetime.date.today()}}
                  ]}
    )
    return orders


def get_request():
    r = requests.get("https://api.covid19api.com/summary")
    j = r.json()
    print(j)


def save_new_order():
    pass
