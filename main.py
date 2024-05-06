from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.directors_vw import directors_ns
from app.views.movies_vw import movies_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)


#
# migrate = Migrate(app, db)


# temp = '{"id": 21, "name": "Тейлор Шеридан"}'
# print(temp)
# print(type(temp))
# temp = director_schema.loads(temp)
# print(temp)
# print(type(temp))


#
# with app.app_context():
#     all_movies = Movie.query.all()
#     movies_schema.dumps(all_movies)
#     print(type(movies_schema))
#     print(movies_schema)

if __name__ == '__main__':
    app = create_app(Config())
    configure_app(app)
    app.run()
