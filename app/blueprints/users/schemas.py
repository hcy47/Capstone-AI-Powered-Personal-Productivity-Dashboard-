from app.extensions import ma
from app.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User


# instantiate the schema

user_schema = UserSchema()
users_schema = UserSchema(many=True) #handle i list of users