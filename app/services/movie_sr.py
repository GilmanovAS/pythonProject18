class MovieService:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        pass

    def get_all(self):
        pass

    def create(self, data):
        pass

    def update(self, data):
        pass

    def delete(self):
        pass

movies = Movie.query
if genre_id:
    movies = movies.filter(genre_id == Movie.genre_id)
if director_id:
    movies = movies.filter(director_id == Movie.director_id)
movies = movies.all()