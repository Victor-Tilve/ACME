# pylint: disable=too-few-public-methods
"The Abstract Processor Interface"
from abc import ABCMeta, abstractmethod


class IProcessor(metaclass=ABCMeta):
    "Abstract Processor Interface"

    @staticmethod
    @abstractmethod
    def load_data(data_queue:list,config:dict):
        "The Abstract Processor Interface method"

    # @staticmethod
    @staticmethod
    @abstractmethod
    def process_data():
        "The Abstract Processor Interface method"

    # @staticmethod
    # @abstractmethod
    # def notify():
    #     "The Abstract Processor Interface method"
