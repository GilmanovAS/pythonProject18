from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return director_service.get_all(), 200

    def post(self):
        data = request.get_json()
        director_service.create(data)
        return 201


@directors_ns.route('/<int:id>')
class DirectorsView(Resource):
    def get(self, id: int):
        return director_service.get_one(id), 200
