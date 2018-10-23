from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from app.api.v1.models.user_model import User

parser = reqparse.RequestParser()
parser.add_argument('email', help='Enter email', required=True, type=str)
parser.add_argument('password', help='Enter password', required=True)


class UserRegistrationEndpoint(Resource):
    def post(self):
        data = parser.parse_args()
        if (data['email'].strip()) and (data['password'].strip()):
            new_user = User(email=data['email'],
                            password=User.generate_hash(data['password'])
                            )
            new_user.save_user()
            return {"message": f'User {data["email"]} was created'}, 201
        return {"message": 'Please enter an email address and password',
                }, 400


class UserLoginEndpoint(Resource):
    def post(self):
        data = parser.parse_args()
        if data['email'].strip() and data['password'].strip():
            if User.fetch_single_user(data['email']):
                current_user = User.fetch_single_user(data['email'])
                if User.verify_hash(data['password'],
                                    current_user["password"]):
                    access_token = create_access_token(identity=data["email"])
                    return{'mesage': f'Logged in as {current_user["email"]}',
                           'access_token': access_token,
                           }, 200
                return {'message': 'Invalid password'}, 400
            return {'message': 'User does not exist'}, 404
        return {"message": "Enter email and password to login"}, 400
