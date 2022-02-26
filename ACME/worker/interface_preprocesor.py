# pylint: disable=too-few-public-methods
"The Abstract Preprocessor Interface"
from abc import ABCMeta, abstractmethod

# COMEBACK:implementar el block queue para organizar cuando leer y cuando esribir en el queue


class IPresprocessor(metaclass=ABCMeta):
    "Abstract Preprocessor Interface"

    @staticmethod
    @abstractmethod
    def load_data(data_queue:list):
        "The Abstract Preprocessor Interface method"

    # @staticmethod
    @staticmethod
    @abstractmethod
    def validate_data():
        "The Abstract Preprocessor Interface method"

    # @staticmethod
    # @abstractmethod
    # def notify():
    #     "The Abstract Preprocessor Interface method"
