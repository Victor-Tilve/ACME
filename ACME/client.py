from employee import Employee
from processor import Processor

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

TRAMAS = [
    'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
    'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
]

days = Processor.load_data(TRAMAS, CONFIG).process_data()
name = Processor.get_employee_name()
Employee.process_day(name, *days)
