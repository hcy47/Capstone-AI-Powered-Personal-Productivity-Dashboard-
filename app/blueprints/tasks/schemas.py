from app.extensions import ma
from app.models import Task


class TaskSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Task
    include_fk = True


# instantiate the schema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True) #handle i list of users