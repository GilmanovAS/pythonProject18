from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import DirectorSchema, Director

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


directors_ns = Namespace('directors')
@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(Director.query.all()), 200

    def post(self):
        temp = request.json
        new_dir = Director(**temp)
        db.session.add(new_dir)
        db.session.commit()
        return 201