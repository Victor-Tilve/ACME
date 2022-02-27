"The abstract Employee Interface"
from abc import ABCMeta, abstractmethod


class IEmployee(metaclass=ABCMeta):
    "Abstract Emproyee Interface"
    @staticmethod
    @abstractmethod
    def process_day(name: str,*args):
        "The abstract Employee interface method"
