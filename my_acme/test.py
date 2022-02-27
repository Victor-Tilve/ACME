"WeekdayDirect Test"
from calendar import THURSDAY, TUESDAY
import unittest
from worker.builder.weekday_director import WeekdayDirector
from worker.factory.day_factory import DayFactory
from worker.preprocesor.preprocessor import Preprocessor
from worker.processor.processor import Processor

CONFIG = {
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

HOURS = {
    "HOUR_SECTION_1": 60,
    "HOUR_SECTION_2": 60,
    "HOUR_SECTION_3": 60,
}
TRAMAS = [
    'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
    'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
    'ASTRID=MO09:00-13:00,TH12:00-14:00,SA20:00-21:00,SU20:00-21:00',
    'ASTRID==MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',  # Wrong structure
    'ASTRID==MO10:00-12:A0,TH12:00-14:00,SU20:00-21:00',  # Wrong structure
    'ASTRID=MO10:00--12:00,TH12:00-14:00,SU20:00-21:00',  # Wrong structure
    'ASTRID=MS10:00-12:00,TH12:00-14:00,SU20:00-21:00',  # Wrong structure
    'ASTRID=MO10:00-12:00,MO12:00-14:00,SU20:00-21:00',  # Wrong structure
]


class MisTests(unittest.TestCase):
    "Test class for DayBuilder"

    def test_weekday_director(self):
        """
        Test that it can sum a list of integers
        """

        MONDAY = WeekdayDirector.construct(CONFIG, HOURS)

        self.assertEqual(MONDAY.get_day_payment(), 60)
        self.assertEqual(MONDAY.get_hour_seccion_1(), 60)
        self.assertEqual(MONDAY.get_hour_seccion_2(), 60)
        self.assertEqual(MONDAY.get_hour_seccion_3(), 60)

    def test_weekend_director(self):
        """
        Test that it can sum a list of integers
        """

        MONDAY = WeekdayDirector.construct(CONFIG, HOURS)

        self.assertEqual(MONDAY.get_day_payment(), 60)
        self.assertEqual(MONDAY.get_hour_seccion_1(), 60)
        self.assertEqual(MONDAY.get_hour_seccion_2(), 60)
        self.assertEqual(MONDAY.get_hour_seccion_3(), 60)

    def test_day_factory(self):
        """
        Test that it can sum a list of integers
        """
        day = "SA"
        saturday = DayFactory.get_day(day=day, config=CONFIG, hours=HOURS)

        self.assertEqual(saturday.get_day_payment(), 75)
        self.assertEqual(saturday.get_hour_seccion_1(), 60)
        self.assertEqual(saturday.get_hour_seccion_2(), 60)
        self.assertEqual(saturday.get_hour_seccion_3(), 60)

    def test_preprocessor(self):
        """
        Testing preprocessor
        """
        trama = TRAMAS[0]
        trama2 = TRAMAS[1]
        trama3 = TRAMAS[2]
        trama4 = TRAMAS[3]
        trama5 = TRAMAS[4]
        trama6 = TRAMAS[5]
        trama7 = TRAMAS[6]
        trama8 = TRAMAS[7]
        
        "If preprocessor return a false that specific set of data is ignore"

        self.assertEqual(Preprocessor.load_data(trama).validate_data(), True)
        self.assertEqual(Preprocessor.load_data(trama2).validate_data(), True)
        self.assertEqual(Preprocessor.load_data(trama3).validate_data(), True)
        self.assertEqual(Preprocessor.load_data(trama4).validate_data(), False)
        self.assertEqual(Preprocessor.load_data(trama5).validate_data(), False)
        self.assertEqual(Preprocessor.load_data(trama6).validate_data(), False)
        self.assertEqual(Preprocessor.load_data(trama7).validate_data(), False)
        self.assertEqual(Preprocessor.load_data(trama8).validate_data(), False)

    def test_processor(self):
        """
        Testing Processor
        """
        "We pick the first data set, RENE"
        trama = TRAMAS[0]
        days = Processor.load_data(trama, CONFIG).process_data()

        MONDAY = days[0]

        self.assertEqual(MONDAY.get_day_payment(), 30)
        self.assertEqual(MONDAY.get_hour_seccion_1(), 0)
        self.assertEqual(MONDAY.get_hour_seccion_2(), 120)
        self.assertEqual(MONDAY.get_hour_seccion_3(), 0)

        TUESDAY = days[1]

        self.assertEqual(TUESDAY.get_day_payment(), 30)
        self.assertEqual(TUESDAY.get_hour_seccion_1(), 0)
        self.assertEqual(TUESDAY.get_hour_seccion_2(), 120)
        self.assertEqual(TUESDAY.get_hour_seccion_3(), 0)

        THURSDAY = days[2]

        self.assertEqual(THURSDAY.get_day_payment(), 50)
        self.assertEqual(THURSDAY.get_hour_seccion_1(), 120)
        self.assertEqual(THURSDAY.get_hour_seccion_2(), 0)
        self.assertEqual(THURSDAY.get_hour_seccion_3(), 0)


if __name__ == '__main__':
    unittest.main()
