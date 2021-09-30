from mongoengine import * 
from mongoengine import Document, StringField , connect
connect(db='white-harbour',host="localhost:27017")


class User(Document):
    username = StringField((max_length=50,required=False)
    email = EmailField(required=True,max_length=50)
    password = StringField(required=True,hidden=True,max_length=50)
    create_at = DateTimeField(max_length=50)
    is_admin = BooleanField()


class Product(Document):
    name = StringField(required=True,max_length=50)
    description = StringField(required=True,max_length=100)
    category = StringField(required=True)
    price = StringField(required=True)
    image = ImageField()
    in_stock = BooleanField()
    count = StringField()
    create_at = DateTimeField()
    

class Category(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    create_at = DateTimeField(required=False)
