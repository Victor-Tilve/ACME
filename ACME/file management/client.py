# pylint: disable=too-few-public-methods
# pylint: disable=missing-final-newline
"Ejemplo de cliente"

from config import Config

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


CONFIGURATION = Config(CONFIG)
print(CONFIGURATION.weekday_hour_section_1_time)
print(CONFIGURATION.weekday_hour_section_1_value)
print(CONFIGURATION.weekday_hour_section_2_time)
print(CONFIGURATION.weekday_hour_section_2_value)
print(CONFIGURATION.weekday_hour_section_3_time)
print(CONFIGURATION.weekday_hour_section_3_value)

print(CONFIGURATION.weekend_hour_section_1_time)
print(CONFIGURATION.weekend_hour_section_1_value)
print(CONFIGURATION.weekend_hour_section_2_time)
print(CONFIGURATION.weekend_hour_section_2_value)
print(CONFIGURATION.weekend_hour_section_3_time)
print(CONFIGURATION.weekend_hour_section_3_value)
