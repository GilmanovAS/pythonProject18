from app.dao.model.movie_md import Movie, MovieSchema
from app.database import db


class MovieDao:
    def __init__(self, session):
        self.session = db.session

    def get_schema(self, data, many=False):
        return MovieSchema(many=many).dump(data)

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get(self, genre_id, director_id):
        movies = self.session.query(Movie)
        if genre_id:
            movies = movies.filter(genre_id == Movie.genre_id)
        if director_id:
            movies = movies.filter(director_id == Movie.director_id)
        return movies.all()

    def create(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, mid):
        self.session.query(Movie).filter(mid == Movie.id).delete()
        self.session.commit()
