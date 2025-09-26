from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from marshmallow import Schema, fields
from model import User

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)

user_blp = Blueprint('User', 'user', description='Operations on users', url_prefix='/user')

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        user_data = [{"id":user.id, "name": user.name, "email": user.email} for user in users]  # Convert to list
        return jsonify(user_data)

    def post(self):
        user_data = request.json
        new_user = User(name=user_data['name'], email=user_data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User successfully created"}), 201

@user_blp.route('/<int:user_id>')
class UsersResource(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({"name": user.name, 'email': user.email})

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json
        user.name = user_data['name']
        user.email = user_data['email']
        db.session.commit()
        return jsonify({"msg": "User successfully updated"}), 201

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "User deleted successfully"}), 201