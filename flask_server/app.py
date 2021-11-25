from flask import Flask, request, Response
from flask_migrate import Migrate
from flask_cors import CORS
from database import db
from database.models import User, Game
from urls.auth import auth_urls
from urls.game import game_urls

app = Flask(__name__)
app.config["SECRET_KEY"] = "eff8dc344027eabe2d0121aaeb0d0885e2c077be6b2c135e59fc592b67c7c56a"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:Mihai10!@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

CORS(app)

app.register_blueprint(auth_urls)
app.register_blueprint(game_urls, url_prefix="/game")
