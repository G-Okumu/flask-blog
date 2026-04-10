from app import app, db
from models.user import User
from models.profile import Profile
from models.blog import Blog
from models.comment import Comment

with app.app_context():
    print("Seeding the database with initial data...")
    User.query.delete()
    Profile.query.delete()
    Comment.query.delete()
    Blog.query.delete()
    db.session.commit() # saves the changes to DB
    
    # seed users
    user1 = User(username='George', email='george@example.com', password_hash='hashed_password')
    user2 = User(username='Lucky', email='lucky@example.com', password_hash='hashed_password')
    
    db.session.add_all([user1, user2])
    db.session.commit()

    # seed profiles
    profile1 = Profile(user_id=user1.id, bio='Software Engineer')
    profile2 = Profile(user_id=user2.id, bio='Data Scientist')

    # seed blogs
    blog1 = Blog(title='My First Blog')
    blog2 = Blog(title='My Second Blog')
    
    db.session.add_all([blog1, blog2])
    db.session.commit()

    comment1 = Comment(content='Great post!', blog_id=blog1.id)
    comment2 = Comment(content='Thanks for sharing!', blog_id=blog2.id)
    

    db.session.add_all([profile1, profile2, comment1, comment2])
    db.session.commit()