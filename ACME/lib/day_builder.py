"The Builder Class"
from typing_extensions import Self
from interface_day_builder import IDayBuilder
from day import Day


class DayBuilder(IDayBuilder):
    "The Day Builder."

    def __init__(self):
        self.day = Day()

    def set_hour_seccion_1(self, hour_seccion_1: int)-> Self:
        "set the hour for an specific section"
        self.day.hour_seccion_1 = hour_seccion_1
        return self

    def set_hour_seccion_2(self, hour_seccion_2: int)-> Self:
        "set the hour for an specific section"
        self.day.hour_seccion_2 = hour_seccion_2
        return self

    def set_hour_seccion_3(self, hour_seccion_3: int) -> Self:  # pylint: disable=undefined-variable
        "set the hour for an specific section"
        self.day.hour_seccion_3 = hour_seccion_3
        return self

    def set_type_of_day(self, weekday: bool)-> Self:
        "Set the type of day, if it is weekday or not"
        self.day.weekday = weekday
        return self

    def get_type_of_day(self)-> bool:
        "get the type of day, if it is weekday or not"
        return self.day.weekday

    def get_result(self, config: dict)-> Day:
        "get all the information that was configure in day object"
        self.day.set_prices(config, self.get_type_of_day())
        return self.day
