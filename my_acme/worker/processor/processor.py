"The preprocessor class"
from .interface_processor import IProcessor
from ..factory.day_factory import DayFactory


class Processor(IProcessor):
    """
    Class preprocessor}
    construct all days indicted in the frame
    """

    data: str = None
    # week_days: dict = None
    section_times = dict()
    config = dict()
    employe_name = ""

    @classmethod
    def load_data(cls, data, config: dict):
        "Method use for loading"

        # COMEBACK: How i implement de block queue system
        cls.data = data

        # NOTE: I asume weekday and weekend always will have identical time sections
        cls.section_times["HOUR_SECTION_1"] = config["WEEKDAY"]["HOUR_SECTION_1"][0]
        cls.section_times["HOUR_SECTION_2"] = config["WEEKDAY"]["HOUR_SECTION_2"][0]
        cls.section_times["HOUR_SECTION_3"] = config["WEEKDAY"]["HOUR_SECTION_3"][0]

        # store the config variable in a class variablo for having acces through classmethod methods
        cls.config = config
        return cls

    @classmethod
    def process_data(cls) -> dict:
        """
        Process data
        """
        created_days = list()
        worked_days = cls._worked_days()
        created_days = cls._create_day(worked_days)
        return created_days

    @classmethod
    def _worked_days(cls) -> list:
        "hacer el docstring"
        # COMEBACK
        colon = ":"
        comma = ","
        equal = "="

        # Validate if _index_finder return a empty list
        if cls._index_finder(cls.data, colon):
            colon_index = cls._index_finder(cls.data, colon)
        else:
            return None

        if cls._index_finder(cls.data, comma):
            comma_index = cls._index_finder(cls.data, comma)
        else:
            return None

        if cls._index_finder(cls.data, equal):
            if len(cls._index_finder(cls.data, equal)) == 1:
                equal_index = cls._index_finder(cls.data, equal)[0]
        else:
            return None

        num_days = 0

        if len(colon_index) % 2 == 0:
            num_days = int(len(colon_index) / 2)
        else:
            return None

        # Day by day extraction
        worked_days = []
        day_1 = cls.data[equal_index+1:comma_index[0]  # pylint: disable=unsubscriptable-object
                         ]
        worked_days.append(day_1)

        for day in range(1, num_days-1):
            worked_days.append(
                cls.data[comma_index[day-1]+1:comma_index[day]])  # pylint: disable=unsubscriptable-object

        day_last = cls.data[comma_index[-1] +   # pylint: disable=unsubscriptable-object
                            1:]
        worked_days.append(day_last)
        cls.employe_name = cls.data[:equal_index]
        return worked_days

    @staticmethod
    def _index_finder(data, find_char: str) -> list:
        "return a list with all the index's matches"
        data_index = [index for index, char in enumerate(
            data) if char == find_char]
        return data_index

    @classmethod
    def _create_day(cls, datas: list) -> list:
        """
        acquire day name
        """
        day_dict = list()
        mins_worked = dict()
        hours = str
        for data in datas:
            # Name extraction

            name = data[:2]
            hours = data[2:]
            mins_worked = cls._process_time(hours, cls.section_times)
            day = DayFactory.get_day(name, cls.config, mins_worked)
            day_dict.append(day)
        return day_dict

    @classmethod
    def _process_time(cls, hours: str, section_times: dict) -> dict:
        """
        calculate the amount of minutes worked in every section
        """
        seccions = dict()
        # Section 1 values
        seccions["HOUR_SECTION_1"] = int(section_times["HOUR_SECTION_1"][0:2]), int(section_times["HOUR_SECTION_1"][3:5]), int(
            section_times["HOUR_SECTION_1"][6:8]), int(section_times["HOUR_SECTION_1"][9:])

        seccions["HOUR_SECTION_2"] = int(section_times["HOUR_SECTION_2"][0:2]), int(section_times["HOUR_SECTION_2"][3:5]), int(
            section_times["HOUR_SECTION_2"][6:8]), int(section_times["HOUR_SECTION_2"][9:])

        seccions["HOUR_SECTION_3"] = int(section_times["HOUR_SECTION_3"][0:2]), int(section_times["HOUR_SECTION_3"][3:5]), int(24 if int(
            section_times["HOUR_SECTION_3"][6:8]) == 0 else int(section_times["HOUR_SECTION_3"][6:8])), int(section_times["HOUR_SECTION_3"][9:])

        # values to process
        start_hour = int(hours[0:2])
        start_min = int(hours[3:5])
        end_hour = int(hours[6:8])
        end_min = int(hours[9:])

        _worked_mins = dict()
        # calculate Secction 1 <>
        _worked_mins["HOUR_SECTION_1"] = cls._calculate_hour_per_section(
            start_hour, start_min, end_hour, end_min, seccions["HOUR_SECTION_1"])
        # calculate Secction 2 <>
        _worked_mins["HOUR_SECTION_2"] = cls._calculate_hour_per_section(
            start_hour, start_min, end_hour, end_min, seccions["HOUR_SECTION_2"])
        # calculate Secction 3 <>
        _worked_mins["HOUR_SECTION_3"] = cls._calculate_hour_per_section(
            start_hour, start_min, end_hour, end_min, seccions["HOUR_SECTION_3"])

        return _worked_mins

    @staticmethod
    # NOTE: i'm not using the leftiest value
    def _calculate_hour_per_section(start_hour: int, start_min: int, end_hour: int, end_min: int, seccion: dict) -> int:
        "Calculete everia minutes the employee works in an specific time"
        # COMEBACK: especial condition for process when someone work till the 24:00
        if start_hour >= seccion[0] and start_hour < seccion[2]:
            if end_hour <= seccion[2]:
                calculate_section_hour = end_hour - start_hour
                if (end_min - start_min) <= 0:
                    calculate_section_1_min = end_min - start_min
                else:
                    calculate_section_hour -= 1
                    calculate_section_1_min = end_min - start_min + 60
            else:
                calculate_section_hour = seccion[2] - start_hour
                if (end_min - start_min) < 0:
                    calculate_section_1_min = end_min - start_min
                else:
                    calculate_section_hour -= 1
                    calculate_section_1_min = end_min - start_min + 60

            calculate_section_1 = calculate_section_hour * 60 + calculate_section_1_min
            return calculate_section_1

        else:
            return 0

    @classmethod
    def get_employee_name(cls):
        return cls.employe_name


if __name__ == "__main__":
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

    TRAMAS = [
        'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
        'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
    ]
    Processor.load_data(TRAMAS[0], CONFIG).process_data()
