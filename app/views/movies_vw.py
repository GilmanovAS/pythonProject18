from flask import request
from flask_restx import Resource, Namespace

from app.database import db

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')

        return (movies_schema.dump(movies), 200)


@movies_ns.route('/<int:id>')
class MoviesView(Resource):
    def get(self, id: int):
        return movie_schema.dump(Movie.query.get(id)), 200

    def delete(self, id: int):
        Movie.query.filter(id == Movie.id).delete()
        db.session.commit()
        return 200
