import datetime
from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    reg_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.datetime.utcnow)
    picture = db.Column(db.String)

    def __init__(self, username: str, password: str, first_name: str, last_name: str, email: str, phone: str, picture: str):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.picture = picture

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'reg_date': self.reg_date.isoformat(),
            'picture': self.picture
        }


class Following(db.Model):
    __tablename__ = "followings"

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True)
    following_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), primary_key=True)

    def __init__(self, user_id: int, following_id: int):
        self.user_id = user_id
        self.following_id = following_id

    def serialize(self):
        return {
            'user_id': self.user_id,
            'following_id': self.following_id
        }


class Mypage(db.Model):
    __tablename__ = "mypages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    introduction = db.Column(db.String(50))

    def __init__(self, user_id: int, introduction: str):
        self.user_id = user_id
        self.introduction = introduction

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'introduction': self.introduction
        }


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    note = db.Column(db.String, nullable=False)
    photo = db.Column(db.String)
    location = db.Column(db.String(50))
    post_date = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.utcnow)

    def __init__(self, user_id: int, note: str, photo: str, location: str):
        self.user_id = user_id
        self.note = note
        self.photo = photo
        self.location = location

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'note': self.note,
            'photo': self.photo,
            'location': self.location,
            'post_date': self.post_date.isoformat()
        }


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(50), nullable=False)
    post_date = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    commenter_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def __init__(self, content: str, commenter_id: int, post_id: int):
        self.content = content
        self.commenter_id = commenter_id
        self.post_id = post_id

    def serialize(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'commenter_id': self.commenter_id,
            'content': self.content,
            'post_date': self.post_date.isoformat()
        }


class Like(db.Model):
    __tablename__ = "likes"

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), primary_key=True)

    def __init__(self, user_id: int, post_id: int):
        self.user_id = user_id
        self.post_id = post_id

    def serialize(self):
        return {
            'user_id': self.user_id,
            'post_id': self.post_id
        }
