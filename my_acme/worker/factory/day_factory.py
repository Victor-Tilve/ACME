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
