import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizard
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(),bcrypt.gensalt())
        id = self.Users.insert({"username": data.username,"name": data.name,"email": data.email,"password": hashed, "about": "Welcome to codewizard", "hobbies": " ", "birthday": "5/12/2001"})
        print("user id is",id)
        myuser = self.Users.find_one({"username": data.username})