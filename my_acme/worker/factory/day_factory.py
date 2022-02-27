# pylint: disable=too-few-public-methods
"Abstract Day Factory"
from ..builder.day import Day
from .interface_day_factory import IDayFactory
from ..builder.weekday_director import WeekdayDirector
from ..builder.weekend_director import WeekendDirector


class DayFactory(IDayFactory):
    "The Abstract Factory Day Class"
    @staticmethod
    def get_day(day: str, config: dict, hours: dict) -> Day:
        "Static get_factory method"
        try:
            if day in ['MO', 'TU', 'WE', 'TH', 'FR']:
                return WeekdayDirector.construct(config, hours)
            if day in ['SA', 'SU']:
                return WeekendDirector.construct(config, hours)
            raise Exception('No Factory Found')
        except Exception as _e:  # pylint: disable=broad-except
            print(_e)
        return None

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
    
    day = "SA"
    SABADO = DayFactory.get_day(day=day,config=config,hours=hours)