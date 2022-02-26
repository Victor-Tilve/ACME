"House Builder Example Code"
from day_factory import DayFactory

CONFIG = {
    "WEEKDAY": {
        "HOUR_SECTION_1": ("00:01-09:00", 25),
        "HOUR_SECTION_2": ("09:01-18:00", 15),
        "HOUR_SECTION_3": ("18:01-00:00", 20),
    },
    "WEEKEND": {
        "HOUR_SECTION_1": ("00:01-09:00", 30),
        "HOUR_SECTION_2": ("00:01-09:00", 20),
        "HOUR_SECTION_3": ("00:01-09:00", 25),
    },
}
worked_hours = {
    "HOUR_SECTION_1":60,
    "HOUR_SECTION_2":60,
    "HOUR_SECTION_3":60,
}
SATURDAY = DayFactory.get_day("Saturday",CONFIG,worked_hours)
MONDAY = DayFactory.get_day("Monday",CONFIG,worked_hours)
print(MONDAY)
print(SATURDAY)

