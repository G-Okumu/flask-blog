from app import ma
from models.blog import Blog
from models.comment import Comment
from marshmallow import fields

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment

    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    blog_id = fields.Int(required=True)

class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    comments = fields.Nested(CommentSchema, many=True)