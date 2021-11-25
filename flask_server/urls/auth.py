import jwt
import json
from datetime import datetime, timedelta
from flask import Response, request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from database.models import User

auth_urls = Blueprint('auth', __name__)


@auth_urls.route("/register/", methods=("POST",))
def register():
    data = request.get_json()

    user = User.query.filter(User.email == data["email"]).first()
    if user:
        return Response(json.dumps({"ok": False}), status=404)

    user = User(
        first_name=data["firstName"],
        last_name=data["lastName"],
        email=data["email"],
        password=generate_password_hash(data["password"])
    )

    db.session.add(user)
    db.session.commit()

    return {
        "ok": True,
    }


@auth_urls.route("/login/", methods=("POST",))
def login():
    data = request.get_json()

    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return Response(json.dumps({"ok": False}), status=404)

    if not check_password_hash(user.password, data['password']):
        return Response(json.dumps({"ok": False}), status=404)

    token = jwt.encode({
        "public_id": user.id,
        "exp": datetime.utcnow() + timedelta(minutes=120)
    }, "eff8dc344027eabe2d0121aaeb0d0885e2c077be6b2c135e59fc592b67c7c56a", algorithm="HS256")

    return {
        "ok": True,
        "token": token,
        "user": {
            "firstName": user.first_name,
            "lastName": user.last_name,
        }
    }
