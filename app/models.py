from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class UserFavs(db.Model):
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