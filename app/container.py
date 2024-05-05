from app.dao.movie_dao import MovieDao
from app.database import db
from app.services.movie_sr import MovieService

movie_dao = MovieDao(db.sesion)
movie_service = MovieService(movie_dao)