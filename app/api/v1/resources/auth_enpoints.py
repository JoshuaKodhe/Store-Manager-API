from flask_restful import Resource, reqparse

from app.api.v1.models.user_model import User
parser = reqparse.RequestParser()
parser.add_argument('username', help='Enter username', required=True)
parser.add_argument('password', help='Enter email', required=True)


parser = reqparse.RequestParser()
parser.add_argument('email', help='Enter email', required=True)
parser.add_argument('password', help='Enter password', required=True)


class UserRegistrationEndpoint(Resource):
    def post(self):
        data = parser.parse_args()
        new_user = User(email=data['email'],
                        password=User.generate_hash(data['password'])
                        )
        new_user.save_user()
        return {"message": f'User {data["email"]} was created',
                }, 201
