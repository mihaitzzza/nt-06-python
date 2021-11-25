from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128))
    wins = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)
    loses = db.Column(db.Integer, default=0)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User, backref="game")
    moves = db.Column(db.JSON, default=[['', '', ''], ['', '', ''], ['', '', '']])
