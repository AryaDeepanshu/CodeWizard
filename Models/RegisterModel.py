import pymongo
from pymongo import MongoClient

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizard
        self.Users = self.db.users

    def insert_user(self, data):
        id = self.Users.insert({"username": data.username,"name": data.name,"email": data.email})
        print("user id is",id)
