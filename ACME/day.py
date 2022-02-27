# pylint: disable=attribute-defined-outside-init

"The Product"


class Day():  # pylint: disable=too-few-public-methods
    "The Product"

    def __init__(self, hour_seccion_1=None, hour_seccion_2=None, hour_seccion_3=None):
        # true, false
        self.hour_seccion_1 = hour_seccion_1
        # true, false
        self.hour_seccion_2 = hour_seccion_2
        # true, false
        self.hour_seccion_3 = hour_seccion_3
        self.weekday: bool = None
        self.day_hour_section_1_price: float = 0  # NOTE: convertir a decimal
        self.day_hour_section_2_price: float = 0  # NOTE: convertir a decimal
        self.day_hour_section_3_price: float = 0  # NOTE: convertir a decimal
        self.prices = dict()

    def process_days(self) -> int:
        "Returns a string describing the construction"
        # COMEBACK: condicional para cuando es la primera hora del día, que se trabajan 59 mins

        self.prices["price_hour_seccion_1"] = float(
            self.hour_seccion_1 * self.day_hour_section_1_price)/60
        self.prices["price_hour_seccion_2"] = float(
            self.hour_seccion_2 * self.day_hour_section_2_price)/60
        self.prices["price_hour_seccion_3"] = float(
            self.hour_seccion_3 * self.day_hour_section_3_price)/60
        payment = self.prices["price_hour_seccion_1"] + self.prices["price_hour_seccion_2"] + self.prices["price_hour_seccion_3"]
        return payment

    def set_prices(self, config: dict, type_of_day: bool):
        "Set prices per hour accoring to the hour secction"
        if type_of_day:
            _type_of_day = "WEEKDAY"
        else:
            _type_of_day = "WEEKEND"

        self.day_hour_section_1_price = config[_type_of_day]["HOUR_SECTION_1"][1]
        self.day_hour_section_2_price = config[_type_of_day]["HOUR_SECTION_2"][1]
        self.day_hour_section_3_price = config[_type_of_day]["HOUR_SECTION_3"][1]

    def get_prices(self):
        "Get the amount of money you have to pay to an employee per secction of time"
        return self.process_days()
