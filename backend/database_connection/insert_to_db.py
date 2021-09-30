import pymongo
from datetime import datetime, date


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["white-harbour"]
user = mydb['user']


def register_user(email,password,confirm_password):
    today = date.today()
    query = {
        "email": email
    }
    doc = user.find_one(query)
    if doc:
        return {email:"email already exists"}
    if password == confirm_password:
        insert_query = {"email":email,"password":password,"created_at":today.strftime("%d/%m/%y"),"is_admin": False}
        user.insert_one(insert_query)
        return {email:"email registered"}
    else:
        return {email:"password doesnot match"}