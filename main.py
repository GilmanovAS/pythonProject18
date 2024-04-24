from flask import Flask, request
from flask_migrate import Migrate
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = True
app.config['DEBUG'] = True

api = Api(app)
api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
movies_ns = api.namespace('movies')
genres_ns = api.namespace('genres')
directors_ns = api.namespace('directors')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')
        movies = Movie.query
        if genre_id:
            movies = movies.filter(genre_id == Movie.genre_id)
        if director_id:
            movies = movies.filter(director_id == Movie.director_id)
        movies = movies.all()
        return (movies_schema.dump(movies), 200)


@movies_ns.route('/<int:id>')
class MoviesView(Resource):
    def get(self, id: int):
        return movie_schema.dump(Movie.query.get(id)), 200

    def delete(self, id: int):
        Movie.query.filter(id == Movie.id).delete()
        db.session.commit()
        return 200


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('gener.id'))
    genre = relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = relationship('Director')
    # foreign_keys = 'Order.customer_id')


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'gener'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class MovieSchema(Schema):
    id = fields.Int(dump_omly=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
gener_schema = GenerSchema()
geners_schema = GenerSchema(many=True)

temp = '{"id": 21, "name": "Тейлор Шеридан"}'
print(temp)
print(type(temp))
temp = director_schema.loads(temp)
print(temp)
print(type(temp))

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(Director.query.all()), 200

    def post(self):
        temp = request.json
        new_dir = Director(**temp)
        db.session.add(new_dir)
        db.session.commit()
        return 201


with app.app_context():
    all_movies = Movie.query.all()
    movies_schema.dumps(all_movies)
    print(type(movies_schema))
    print(movies_schema)

if __name__ == '__main__':
    app.run()
