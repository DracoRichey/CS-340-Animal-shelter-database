#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient

class CRUD:
    def __init__(self):
        user = 'aacuser'
        password = 'SNHUuser123'
        host = 'nv-desktop-services.apporto.com'
        port = 33382
        db_name = 'AAC'
        collection_name = 'animals'

        # Initialize MongoDB connection
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        if data:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, key, value):
        cursor = self.collection.find({key: value})
        results = list(cursor)
        return results if results else []
    
    def update(self, key, value, new_data):
        result = self.collection.update_many({key: value}, {"$set": new_data})
        return result.modified_count

    def delete(self, key, value):
        result = self.collection.delete_many({key: value})
        return result.deleted_count

