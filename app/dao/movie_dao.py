from app.dao.model.movie_md import Movie, MovieSchema
from app.database import db


class MovieDao:
    def __init__(self, session):
        self.session = db.session

    def get_schema(self, data, many=False):
        return MovieSchema(many=many).dump(data)
    def load_schema(self, data):
        return MovieSchema().load(data)

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get(self, genre_id, director_id, year):
        movies = self.session.query(Movie)
        if genre_id:
            movies = movies.filter(genre_id == Movie.genre_id)
        if director_id:
            movies = movies.filter(director_id == Movie.director_id)
        if year:
            movies = movies.filter(year == Movie.year)
        return movies.all()

    def create(self, data):
        self.session.add(Movie(**data))
        self.session.commit()
        self.session.close()


    def update(self, data):
        self.session.add(data)
        self.session.commit()
        self.session.close()

    def delete(self, mid):
        self.session.query(Movie).filter(mid == Movie.id).delete()
        self.session.commit()
