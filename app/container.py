from app.dao.director_dao import DirectorDao
from app.dao.movie_dao import MovieDao
from app.database import db
from app.services.director_sr import DirectorService
from app.services.movie_sr import MovieService

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)
