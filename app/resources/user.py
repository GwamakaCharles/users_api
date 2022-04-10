from flask_restful import Resource
from models.user import UserModel

class Users(Resource):

    def get(self):
        return {'users' : [user.json() for user in UserModel.query.paginate().items]}
        
class User(Resource):

    def get(self,name):
        user = UserModel.find_user_by_name(name)
        return user.json()
