import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(String(250), nullable=False)

    def to_dict(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id 
        }


class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, primary_key=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email 
        }
    

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id 
        }


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(enumerate(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id 
        }


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')