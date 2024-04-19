from flask import Flask, request
from marshmallow import Schema, fields
from flask_migrate import Migrate
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FSADASDF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['JSON_AS_ASCII'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBAG'] = True

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
