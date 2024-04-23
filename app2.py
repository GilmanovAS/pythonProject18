from flask import Flask, request
from flask_migrate import Migrate
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SADFSA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}

movies_ns = api.namespace('movies')
genres_ns = api.namespace('genres')
directors_ns = api.namespace('directors')


class MoviesSchema(Schema):
    id = fields.Int(dump_omly=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class GenreSchema(Schema):
    id = fields.Int(dump_omly=True)
    name = fields.Str()


class DirectorSchema(Schema):
    id = fields.Int(dump_omly=True)
    name = fields.Str()


class MovieDB(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer())
    rating = db.Column(db.Float())
    genre_id = db.Column(db.Integer(), db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer(), db.ForeignKey('director.id'))
    genre = relationship('GenreDB')
    director = relationship('DirectorDB')


class DirectorDB(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class GenreDB(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')
        movies_schema = MoviesSchema(many=True)
        movies_all = MovieDB.query
        if genre_id:
            movies_all = movies_all.filter(genre_id == MovieDB.genre_id)
        if director_id:
            movies_all = movies_all.filter(director_id == MovieDB.director_id)
        return movies_schema.dump(movies_all.all()), 200

if __name__ == '__main__':
    app.run()
