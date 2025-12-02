#where i will initialize SQLAlchemy and  create my models

from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, String, Table, Column, ForeignKey, DateTime, Float, Integer,Boolean


#create base models to be inherited from
class Base(DeclarativeBase):
  pass

#instantiate your sqlalchemy database:
db = SQLAlchemy(model_class=Base)

class User(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key= True)
  name: Mapped[str] = mapped_column(String(60),nullable=False)
  last_name: Mapped[str] = mapped_column(String(60),nullable=False)
  email: Mapped[str] = mapped_column(String(60),nullable=False, unique=True)
  password: Mapped[str] = mapped_column(String(500),nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)

# relationships
  categories: Mapped[list['Category']]= relationship('Category', back_populates='user')
  tasks: Mapped[list['Task']] = relationship('Task', back_populates='user')
  ai_recommendations: Mapped[list['Ai_recommendation']] = relationship('Ai_recommendation', back_populates='user')
  task_history: Mapped[list["Task_history"]] = relationship("Task_history", back_populates="user")




class Task(Base):
  __tablename__= 'tasks'

  id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
  category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
  title: Mapped[str] = mapped_column(String(100), nullable=False)
  description: Mapped[str] = mapped_column(String(300))
  priority: Mapped[int] = mapped_column(Integer, default=1)  
  due_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
  is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
  updated_at: Mapped[datetime] = mapped_column(
  DateTime, default=datetime.now, onupdate=datetime.now)

  # RELATIONSHIPS
  user: Mapped["User"] = relationship("User", back_populates="tasks")
  category: Mapped["Category"] = relationship("Category", back_populates="tasks")
  ai_recommendations: Mapped[list["Ai_recommendation"]] = relationship(
  "Ai_recommendation", back_populates="task")
  task_history: Mapped[list['Task_history']]= relationship('Task_history', back_populates='task')




class Category(Base):
  __tablename__= 'categories'

  id: Mapped[int]= mapped_column(primary_key= True)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
  name: Mapped[str] = mapped_column(String(300), nullable=False)
  category_name: Mapped[str] = mapped_column(String(300), nullable=False)

  # relationships
  user: Mapped['User']= relationship('User', back_populates='categories')
  tasks: Mapped[list['Task']] = relationship('Task', back_populates='category')





class Ai_recommendation(Base):
  __tablename__= 'recommendations'

  id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
  task_id: Mapped[int]= mapped_column(ForeignKey('tasks.id'), nullable=False)
  recommended_time: Mapped[datetime]= mapped_column(DateTime,  default=datetime.now(), nullable=False)
  confidence: Mapped[float]= mapped_column(Float, nullable=False)
  generated_at: Mapped[datetime]= mapped_column(DateTime, default=datetime.now(), nullable=False)

  # relationships
  user: Mapped["User"] = relationship("User", back_populates="ai_recommendations")
  task: Mapped["Task"] = relationship("Task", back_populates="ai_recommendations")





class Task_history(Base):
  __tablename__= 'task_histories'

  id: Mapped[int] = mapped_column(primary_key=True)
  task_id: Mapped[int]= mapped_column(ForeignKey('tasks.id'), nullable=False)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
  completed_at: Mapped[datetime]= mapped_column(DateTime, default=datetime.now())

  # relationships
  user: Mapped["User"] = relationship("User", back_populates="task_history")
  task: Mapped["Task"] = relationship("Task", back_populates='task_history')
