from mongoengine import *
connect(db='port-white',host="localhost:27017")

class User(Document):
    username = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True,hidden=True)
    create_at = DateTimeField()
    updated_at = DateTimeField()
    is_admin = BooleanField()

# class Product(Document):
#     username = StringField(required=True)
#     email = EmailField(required=True)
#     password = PasswordField(required=True)
#     create_at = DateTimeField(required=True)
#     updated_at = DateTimeField(required=True)
    
# class Category(Document):
#     username = StringField(required=True)
#     email = EmailField(required=True)
#     password = PasswordField(required=True)
#     create_at = DateTimeField(required=True)
#     updated_at = DateTimeField(required=True)

# User(username="admin").save()

