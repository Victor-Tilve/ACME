"A Director Class"
from .day_builder import DayBuilder


class WeekendDirector:  # pylint: disable=too-few-public-methods
    """One of the Directors, that can build a complex representation. 
    So far, it's able to build weekend"""
    @staticmethod
    # COMEBACK: no he desarrollado como meteré las horas
    def construct(config: dict, hours: dict):
        "Procesaría que cantidad de tiempo iría a cada sección de horas"

        # NOTE: No sería un valor tipo bool sino una tupla con minutos y segundos
        return DayBuilder()\
            .set_hour_seccion_1(hours["HOUR_SECTION_1"])\
            .set_hour_seccion_2(hours["HOUR_SECTION_2"])\
            .set_hour_seccion_3(hours["HOUR_SECTION_3"])\
            .set_type_of_day(False)\
            .get_result(config)
