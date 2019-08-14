class BaseService:
    ma = None

    def init_marshmallow(self, ma):
        self.ma = ma

    def get_marshmallow(self):
        return self.ma
