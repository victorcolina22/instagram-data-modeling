import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    firstname = Column(String(255))
    lastname = Column(String(255))
    email = Column(String(255))

    
class Follower(Base):
    __tablename__ = 'followers'
    users_from_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    users_to_id = Column(Integer, ForeignKey('users.id'), primary_key=True)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))


class Media(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    media_type = Column(Integer)
    media_url = Column(String(255))
    posts_id = Column(Integer, ForeignKey('posts.id'))


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(300), nullable=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    posts_id = Column(Integer, ForeignKey('posts.id'))


    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')