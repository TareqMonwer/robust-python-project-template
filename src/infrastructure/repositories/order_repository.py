from pymongo import MongoClient


class OrderRepository:
    def __init__(self, mongo_client: MongoClient):
        self.collection = mongo_client["orders"]

    def save(self, order_data):
        result = self.collection.insert_one(order_data)
        return str(result.inserted_id)

    def get_order(self, order_id):
        return self.collection.find_one({"_id": order_id})
