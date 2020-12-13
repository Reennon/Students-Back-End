from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource
import main


class LoginResource(Resource):
    """
    GET endpoint
    """

    def post(self):

        if not request.is_json:
            return 400
        json = request.get_json()
        username = json["username"]
        password = json["password"]
        if not username or not password:
            return 400

        access_token = create_access_token(identity=username, expires_delta=False)
        return str(access_token), 200
