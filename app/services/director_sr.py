from app.dao.director_dao import DirectorDao


class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_schema(self.director_dao.get_all(), many=True)

    def get_one(self, did):
        return self.director_dao.get_schema(self.director_dao.get_one(did), many=False)

    def create(self, data):
        self.director_dao.create(self.director_dao.load_schema(data))
