import pymongo
from pymongo import MongoClient
import bcrypt

class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizard
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        inserted = self.Posts.insert({"username": data.username, "content": data.content})
        return True

    
    def get_all_post(self):
        all_posts = self.Posts.find()
        new_posts = []
        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            new_posts.append(post)
        return new_posts
    
    
    def get_user_post(self,user):
        all_posts = self.Posts.find({"username":user}).sort("date_added",-1)
        new_posts = []
        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            new_posts.append(post)
        return new_posts