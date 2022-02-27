# pylint: disable=too-few-public-methods
"The Abstract Factory Interface"
from abc import ABCMeta, abstractmethod


class IDayFactory(metaclass=ABCMeta):
    "Abstract Day Factory Interface"

    @staticmethod
    @abstractmethod
    def get_day(day: str, config: dict, hours: dict):
        "The static Abstract factory interface method"
