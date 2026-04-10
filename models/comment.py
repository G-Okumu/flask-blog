from app import db

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    blog = db.relationship('Blog', back_populates='comments')

    def __repr__(self):
        return f'<Comment {self.content}>'