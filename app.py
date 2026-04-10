import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, jsonify
from config import Config


pymysql.install_as_MySQLdb()

app = Flask(__name__) # initializing the Flask application
app.config.from_object(Config) # import db configurations

db = SQLAlchemy(app) # initializing the SQLAlchemy object with the Flask app, which allows us to interact with the database using SQLAlchemy's ORM features.
ma = Marshmallow(app)


from models.user import User
from models.profile import Profile
from models.comment import Comment
from models.blog import Blog
from schemas.user_schema import UserSchema
from schemas.blog_schema import BlogSchema

def create_tables():
    with app.app_context():
        db.create_all()
        
    print("Tables created successfully.")

create_tables()
    
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users))

@app.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.all()
    blog_schema = BlogSchema(many=True)
    return jsonify(blog_schema.dump(blogs))

if __name__ == '__main__':
    app.run(debug=True)