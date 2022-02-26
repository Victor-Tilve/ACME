# pylint: disable=too-few-public-methods
"Abstract Furniture Factory"
from day import Day
from interface_day_factory import IDayFactory
from weekday_director import WeekdayDirector
from weekend_director import WeekendDirector


class DayFactory(IDayFactory):
    "The Abstract Factory Concrete Class"
    @staticmethod
    def get_day(day: str, config: dict, hours: dict) -> Day:
        "Static get_factory method"
        try:
            if day in ['Monday', 'Tusday', 'Wednesdy', 'Thursday', 'Friday']:
                return WeekdayDirector.construct(config, hours)
            if day in ['Saturday', 'Sunday']:
                return WeekendDirector.construct(config, hours)
            raise Exception('No Factory Found')
        except Exception as _e:  # pylint: disable=broad-except
            print(_e)
        return None
