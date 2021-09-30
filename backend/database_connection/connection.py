from mongoengine import *
connect(db='white-harbour',host="localhost:27017")

class User(Document):
    username = StringField()
    email = EmailField(required=True)
    password = StringField(required=True,hidden=True)
    create_at = DateTimeField()
    is_admin = BooleanField()
    session_token = StringField(default=0)

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


