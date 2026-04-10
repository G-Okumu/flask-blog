import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from config import Config



pymysql.install_as_MySQLdb()

app = Flask(__name__) # initializing the Flask application
app.config.from_object(Config) # import db configurations

db = SQLAlchemy(app) # initializing the SQLAlchemy object with the Flask app, which allows us to interact with the database using SQLAlchemy's ORM features.



from models.user import User
from models.profile import Profile
from models.comment import Comment
from models.blog import Blog

def create_tables():
    with app.app_context():
        db.create_all()
        
    print("Tables created successfully.")

create_tables()
    
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all() # Querying all User records from the database using SQLAlchemy's query interface. The result is a list of User objects.
    return jsonify([{ "username": user.username, "email": user.email , "profile": {"bio":user.profile.bio}} for user in users])

@app.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.all()
    blogs_list = [
        {
            "id": blog.id,
            "title": blog.title,
            "comments": [
                {"id": comment.id, "text": comment.content} for comment in blog.comments
            ]
        } for blog in blogs
    ]
    return jsonify(blogs_list)

if __name__ == '__main__':
    app.run(debug=True)