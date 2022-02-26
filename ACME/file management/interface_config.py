# pylint: disable=too-few-public-methods
"A Config Interface"
from abc import ABCMeta, abstractmethod


class IConfig(metaclass=ABCMeta):

    "A Config Interface"
    @staticmethod
    @abstractmethod
    def get_property(property_name):
        "Must implement add_winner"
