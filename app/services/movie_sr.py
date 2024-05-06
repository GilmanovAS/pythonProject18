class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_one(self, mid):
        return self.movie_dao.get_schema(self.movie_dao.get_one(mid))

    def get(self, genre_id, director_id):
        return self.movie_dao.get_schema(self.movie_dao.get(genre_id, director_id), many=True)

    def create(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, mid):
        self.movie_dao.delete(mid)

# movies = Movie.query
# if genre_id:
#     movies = movies.filter(genre_id == Movie.genre_id)
# if director_id:
#     movies = movies.filter(director_id == Movie.director_id)
# movies = movies.all()
