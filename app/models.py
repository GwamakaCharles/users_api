from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Resource

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))

    def __init__(self,name):
        self.name = name        

    def json(self):
        return {'name': self.name}

    @classmethod
    def find_user_by_name(cls,name): 
       return cls.query.filter_by(name=name).first_or_404()

class Users(Resource):
    
    def get(self):
        return {'users' : [user.json() for user in UserModel.query.paginate().items]}
        
class User(Resource):

    def get(self,name):
        user = UserModel.find_user_by_name(name)
        return user.json()
