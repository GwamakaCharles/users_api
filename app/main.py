from flask import Flask, request, render_template
from flask_restful import Api
import redis

app = Flask(__name__)
api = Api(app)


# postgresql://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev'

from models import db, UserFavs

@app.before_first_request
def create_tables():
    db.create_all()

red = redis.Redis(host='redis', port=6379, db=0)

# @app.route("/")
# def main():
#     return render_template('index.html')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)