from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile = db.relationship('Profile', uselist=False, back_populates='user')
    

    def __repr__(self):
        return f'<User {self.username}>'
    
    
# backref  - a short cut for backpopulates, you define the relationship mapping on one side only.
# user1.profile()