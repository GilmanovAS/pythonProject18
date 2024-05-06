from flask import request
from flask_restx import Resource, Namespace



directors_ns = Namespace('directors')
@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        pass
        # return directors_schema.dump(Director.query.all()), 200

    def post(self):
        pass
        # temp = request.json
        # new_dir = Director(**temp)
        # db.session.add(new_dir)
        # db.session.commit()
        # return 201