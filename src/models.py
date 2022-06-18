import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class  User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    addresses = relationship('Post', backref='user', lazy=True)


class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(String(250), nullable=False)
    photo = Column(String(250), nullable=False)
    addresses = relationship('Post', backref='follower', lazy=True)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    text = Column(String(250), nullable=False)
    icons = Column(String(250), nullable=False)
    diameter = relationship('Post', backref='comment', lazy=True)


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    facebook = Column(String(250), nullable=False)
    twitter = Column(String(250), nullable=False)
    youtube = Column(String(250), nullable=False)
    cost = relationship('Post', backref='media', lazy=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    follower_id = Column(Integer, ForeignKey('follower.id'),
        nullable=False)
    comment_id = Column(Integer, ForeignKey('comment.id'),
        nullable=False)
    media_id = Column(Integer, ForeignKey('media.id'),
        nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e