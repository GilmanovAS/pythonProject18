from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')
        year = request.args.get('year')
        movies = movie_service.get(genre_id, director_id, year)
        return movies, 200

    def post(self):
        data = request.get_json()
        movie_service.create(data)
        return 200


@movies_ns.route('/<int:id>')
class MoviesView(Resource):
    def get(self, id: int):
        return movie_service.get_one(id), 200

    def put(self, id: int):
        data = request.get_json()
        return movie_service.update(id, data), 200

    def delete(self, id: int):
        movie_service.delete(id)
        return 200
