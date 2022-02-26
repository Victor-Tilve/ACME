"The Builder Interface"
from abc import ABCMeta, abstractmethod


class IDayBuilder(metaclass=ABCMeta):
    "The Day Builder Interface"
    @staticmethod
    @abstractmethod
    def set_hour_seccion_1(hour_seccion_1: int):
        "Build hour_seccion_1"
    @staticmethod
    @abstractmethod
    def set_hour_seccion_2(hour_seccion_2: int):
        "Build hour_seccion_2"

    @staticmethod
    @abstractmethod
    def set_hour_seccion_3(hour_seccion_3: int):
        "Number of hour_seccion_3"

    @staticmethod
    @abstractmethod
    def set_type_of_day(weekday: bool):
        "Type of day of the week, "

    @staticmethod
    @abstractmethod
    def get_result(config: dict):
        "Return the final product"
