"Configuracion especifica"
from config import Config

class MongoConfig(Config):
    "Ejemplo para poner en practica"

    @property
    def host(self):
        "Ejemplo para poner en practica"
        return self.get_property('MONGO_HOST')

    @property
    def port(self):
        "Ejemplo para poner en practica"
        return self.get_property('MONGO_PORT')

    @property
    def username(self):
        "Ejemplo para poner en practica"
        return self.get_property('MONGO_USERNAME')

    @property
    def db_name(self):
        "Ejemplo para poner en practica"
        return self.get_property('MONGO_DB_NAME')

    @property
    def password(self):
        "Ejemplo para poner en practica"
        return self.get_property('MONGO_PASSWORD')