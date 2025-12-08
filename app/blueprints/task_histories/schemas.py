from app.extensions import ma
from app.models import Task_history

class TaskHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task_history
        include_fk = True

task_history_schema = TaskHistorySchema()
task_histories_schema = TaskHistorySchema(many=True)
