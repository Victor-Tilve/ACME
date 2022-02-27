"The preprocessor class"
from interface_preprocesor import IPresprocessor


class Preprocessor(IPresprocessor):
    "Class preprocessor"

    data: str = None

    @classmethod
    def load_data(cls, data_queue):
        "Method use for loading data"
        cls.data = data_queue
        return cls

    @classmethod
    def validate_data(cls) -> bool:
        """
        Method use for validating data
        - num of days: every day has 2 colom in its secction, if it is no the case
        thej frame will be ignore.
        - the number of commas must be one les than the number of colon divided by 2
        - it's not allow repite a day of the week for a work schedule employee, maximum 7 fields of day worked
        - one day is define between 00:01-24:00
        """

        worked_day = cls._worked_day()
        if worked_day is None:
            print("not follow the frame structure")
            return False
        
        if not cls._validate_day_names(worked_day):
            print("not Follow no-repetition day name rule")
            return False
        
        if not cls._validate_hour_structure(worked_day):
            print("not Follow the hour structure")
            return False
        
        return True

    @classmethod
    def _worked_day(cls) -> list:
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
        worked_day = []
        day_1 = cls.data[equal_index+1:comma_index[0]] #pylint: disable=unsubscriptable-object
        worked_day.append(day_1)

        for day in range(1, num_days-1):
            worked_day.append(cls.data[comma_index[day-1]+1:comma_index[day]])#pylint: disable=unsubscriptable-object

        day_last = cls.data[comma_index[-1]+1:] #pylint: disable=unsubscriptable-object
        worked_day.append(day_last)

        return worked_day

    @staticmethod
    def _index_finder(data, find_char: str) -> list:
        "return a list with all the index's matches"
        data_index = [index for index, char in enumerate(
            data) if char == find_char]
        return data_index

    @staticmethod
    def _validate_day_names(day_schedules: list) -> bool:
        """
        - validate the names of the week follow de convention:
            MO: Monday
            TU: Tuesday
            WE: Wednesday
            TH: Thursday
            FR: Friday
            SA: Saturday
            SU: Sunday
        - Make sure there is not repeted name of the week in an specific scheduled week

        """
        day_counter = {
            "MO": 0,
            "TU": 0,
            "WE": 0,
            "TH": 0,
            "FR": 0,
            "SA": 0,
            "SU": 0,
        }

        for day_schedule in day_schedules:
            # Name extraction
            name = day_schedule[:2]
            # print(f"Nombre:{name}")
            if name not in day_counter.keys():
                return False
            else:
                day_counter[name] += 1

        for _, day_count in day_counter.items():
            if day_count > 1:
                return False

        return True

    @classmethod
    def _validate_hour_structure(cls, day_schedules: list) -> bool:
        for day_schedule in day_schedules:
            # Hour extraction
            hour = day_schedule[2:]
            colon = ":"
            dash = "-"
            colon_index = cls._index_finder(day_schedule, colon)
            dash_index = cls._index_finder(day_schedule, dash)
            start_hour = day_schedule[2:4]
            start_min = day_schedule[5:7]
            end_hour = day_schedule[8:10]
            end_min = day_schedule[11:]

            # Must have 11 characters
            if len(hour) != 11:
                return False
            elif len(colon_index) != 2:
                return False
            elif len(dash_index) != 1:
                return False
            elif not start_hour.isdigit() or not start_min.isdigit() or not end_hour.isdigit() or not end_min.isdigit():
                return False
            return True


if __name__ == "__main__":
    TRAMAS = [
        'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
        'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
    ]
    trama = TRAMAS.pop(0)
    print(Preprocessor.load_data(trama).validate_data())
