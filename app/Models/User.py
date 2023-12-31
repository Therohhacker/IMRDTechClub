from app.db import db

class User(db.Model):
    __tablename__ = "user"

    uid = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    