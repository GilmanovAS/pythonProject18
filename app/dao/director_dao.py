# director_schema = DirectorSchema()
# directors_schema = DirectorSchema(many=True)
from app.dao.model.director_md import Director, DirectorSchema
from app.database import db


class DirectorDao:
    def __init__(self, session):
        self.session = db.session

    def get_schema(self, data, many=False):
        return DirectorSchema(many=many).dump(data)

    def load_schema(self, data):
        return DirectorSchema().load(data)
    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def create(self, data):
        self.session.add(Director(**data))
        self.session.commit()
        self.session.close()





