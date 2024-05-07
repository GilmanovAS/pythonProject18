from app.dao.movie_dao import MovieDao


class MovieService:
    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    def get_one(self, mid):
        return self.movie_dao.get_schema(self.movie_dao.get_one(mid))

    def get(self, genre_id, director_id, year):
        return self.movie_dao.get_schema(self.movie_dao.get(genre_id, director_id, year), many=True)

    def create(self, data):
        self.movie_dao.create(self.movie_dao.load_schema(data))

    def update(self, mid, data):
        json_data = self.movie_dao.load_schema(data)
        print(json_data)
        movie = self.movie_dao.get_one(mid)
        movie.title = json_data['title']
        movie.description = json_data['description']
        movie.trailer = json_data['trailer']
        movie.year = json_data['year']
        movie.rating = json_data['rating']
        movie.genre_id = json_data['genre_id']
        movie.director_id = json_data['director_id']
        self.movie_dao.update(movie)

    def delete(self, mid):
        self.movie_dao.delete(mid)

# movies = Movie.query
# if genre_id:
#     movies = movies.filter(genre_id == Movie.genre_id)
# if director_id:
#     movies = movies.filter(director_id == Movie.director_id)
# movies = movies.all()
