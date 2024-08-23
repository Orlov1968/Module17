from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.models.task import Task


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    task = relationship("Task", back_populates="users")
