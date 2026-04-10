from app import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #  this is where the relationship exists
    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f'<Profile {self.name}>'