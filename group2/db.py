from pymongo import MongoClient


class DB:
    def __init__(self, host, db_name="egeos_db", collection_name="events") -> None:
        self.client = MongoClient(host)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, events):
        self.collection.insert_many(events)

    def get_events(self, start_date=None, end_date=None):
        print(start_date[:10], end_date[:10])
        query = {}
        if start_date or end_date:
            query["date"] = {}
        if start_date:
            query["date"]["$gte"] = start_date[:10]
        if end_date:
            query["date"]["$lt"] = end_date[:10]
        cursor = self.collection.find(query)
        results = [self.serialize_event(doc) for doc in cursor]
        if results:
            results["images"] = [img for img in results["images"] if start_date <= img["date"] < end_date]
        return results

    @staticmethod
    def serialize_event(doc):
        return {
            "event_id": doc["event_id"],
            "type": doc["type"],
            "country": doc["country"],
            "date": doc["date"],
            "locations": doc["locations"],
            "timeframe": doc["timeframe"],
            "images": doc["images"]
        }
