"A Director Class"
from .day_builder import DayBuilder


class WeekdayDirector:  # pylint: disable=too-few-public-methods
    """One of the Directors, that can build a complex representation. 
    So far, it's able to build weekdays"""
    @staticmethod
    # COMEBACK: no he desarrollado como meteré las horas
    def construct(config: dict, hours: dict):
        "Procesaría que cantidad de tiempo iría a cada sección de horas"

        # NOTE: No sería un valor tipo bool sino una tupla con minutos y segundos
        return DayBuilder()\
            .set_hour_seccion_1(hours["HOUR_SECTION_1"])\
            .set_hour_seccion_2(hours["HOUR_SECTION_2"])\
            .set_hour_seccion_3(hours["HOUR_SECTION_3"])\
            .set_type_of_day(True)\
            .get_result(config)


if __name__ == "__main__":
    config = {
        "WEEKDAY": {
            "HOUR_SECTION_1": ("00:01-09:00", 25),
            "HOUR_SECTION_2": ("09:01-18:00", 15),
            "HOUR_SECTION_3": ("18:01-00:00", 20),
        },
        "WEEKEND": {
            "HOUR_SECTION_1": ("00:01-09:00", 30),
            "HOUR_SECTION_2": ("09:01-18:00", 20),
            "HOUR_SECTION_3": ("18:01-00:00", 25),
        },
    }

    hours = {
        "HOUR_SECTION_1": 60,
        "HOUR_SECTION_2": 60,
        "HOUR_SECTION_3": 60,
    }

    LUNES = WeekdayDirector.construct(config, hours)
