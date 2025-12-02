from app.extensions import ma
from app.models import Category


class CategorySchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Category
    include_fk = True


# instantiate the schema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True) #handle i list of users