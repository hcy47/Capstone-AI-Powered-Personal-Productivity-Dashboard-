#where i will initialize SQLAlchemy and  create my models

from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, String, Table, Column, ForeignKey, DateTime, Float, Integer


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

  categories: Mapped[list['Category']]= relationship('Category', back_populates='user')


class Category(Base):
  __tablename__= 'categories'

  id: Mapped[int]= mapped_column(primary_key= True)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
  name: Mapped[str] = mapped_column(String(300), nullable=False)
  category_name: Mapped[str] = mapped_column(String(300), nullable=False)

  user: Mapped['User']= relationship('User', back_populates='categories')


# class Ai_recommendation(Base):