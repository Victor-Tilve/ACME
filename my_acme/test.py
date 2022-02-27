"WeekdayDirect Test"
import unittest
from worker.builder.weekday_director import WeekdayDirector




class MisTests(unittest.TestCase):
    "Test class for DayBuilder"

    def test_weekday_director(self):
        """
        Test that it can sum a list of integers
        """
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

        self.assertEqual(LUNES.get_day_payment(), 60)
        self.assertEqual(LUNES.get_hour_seccion_1(), 60)
        self.assertEqual(LUNES.get_hour_seccion_2(), 60)
        self.assertEqual(LUNES.get_hour_seccion_3(), 60)

    def test_weekend_director(self):
        """
        Test that it can sum a list of integers
        """
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

        self.assertEqual(LUNES.get_day_payment(), 60)
        self.assertEqual(LUNES.get_hour_seccion_1(), 60)
        self.assertEqual(LUNES.get_hour_seccion_2(), 60)
        self.assertEqual(LUNES.get_hour_seccion_3(), 60)


if __name__ == '__main__':
    unittest.main()
