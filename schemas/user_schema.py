from app import ma
from models.user import User
from models.profile import Profile
from marshmallow import fields

class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        include_fk = True
        load_instance = True

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

    profile = fields.Nested(ProfileSchema)