# from flask_restful import Resource, Api

from flask import request
from flask import Response, request
from backend.database_connection.connection import User
# from flask_jwt_extended import create_access_token
# from database.models import User
# from flask_restful import Resource 
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        User("name"=name)
        user.save()
        id = user.id
        return {'id': str(id)}, 200