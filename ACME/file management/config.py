# pylint: disable=too-few-public-methods
# pylint: disable=missing-final-newline
# pylint: disable=consider-iterating-dictionary
# loaded config
"Archivo de configuracion"
#NOTE:"importarlo desde el YAML"

from interface_config import IConfig

class Config(IConfig):
    "The Config as a Singleton"
    _config = {}

    def __new__(cls, config):
        cls._config = config
        return cls

    @classmethod
    def get_property(cls, property_name):
        "get the properties of the configuration "

        if property_name not in cls._config.keys():  # we don't want KeyError
            return None  # just return None if not found
        return cls._config[property_name]

    @classmethod
    @property
    def weekday_hour_section_1_time(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKDAY')["HOUR_SECTION_1"][0]

    @classmethod
    @property
    def weekday_hour_section_1_value(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKDAY')["HOUR_SECTION_1"][1]

    @classmethod
    @property
    def weekday_hour_section_2_time(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKDAY')["HOUR_SECTION_2"][0]

    @classmethod
    @property
    def weekday_hour_section_2_value(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKDAY')["HOUR_SECTION_2"][1]

    @classmethod
    @property
    def weekday_hour_section_3_time(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKDAY')["HOUR_SECTION_3"][0]

    @classmethod
    @property
    def weekday_hour_section_3_value(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKDAY')["HOUR_SECTION_3"][1]
    
    @classmethod
    @property
    def weekend_hour_section_1_time(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKEND')["HOUR_SECTION_1"][0]

    @classmethod
    @property
    def weekend_hour_section_1_value(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKEND')["HOUR_SECTION_1"][1]

    @classmethod
    @property
    def weekend_hour_section_2_time(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKEND')["HOUR_SECTION_2"][0]

    @classmethod
    @property
    def weekend_hour_section_2_value(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKEND')["HOUR_SECTION_2"][1]

    @classmethod
    @property
    def weekend_hour_section_3_time(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKEND')["HOUR_SECTION_3"][0]

    @classmethod
    @property
    def weekend_hour_section_3_value(cls):
        "Ejemplo para poner en practica"
        return cls.get_property('WEEKEND')["HOUR_SECTION_3"][1]