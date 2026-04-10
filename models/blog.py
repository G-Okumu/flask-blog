from app import db

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    comments = db.relationship('Comment', back_populates='blog') 

    def __repr__(self):
        return f'<Blog {self.title}>'