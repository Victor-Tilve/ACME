"Main script"
import sys

from worker.preprocesor.preprocessor import Preprocessor
from worker.processor.processor import Processor
from employee.employee import Employee
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

def read_file(path):
    "Funtion to open and read information for txt file"
    input_sentences = []
    with open(path, "r") as f:
        input_sentences = f.readlines()

    return input_sentences


def main(argv):
    "Main method. run all the modules"
    input_sentences = list()

    if len(argv) != 1:
        print("Something went wrong")
        sys.exit()
    else:
        path = argv[0]
        input_sentences = read_file(path)

    for sentence in input_sentences:
        sentence = sentence.rstrip("\n")
        if Preprocessor.load_data(sentence).validate_data():
            days = Processor.load_data(sentence, CONFIG).process_data()
            name = Processor.get_employee_name()
            Employee.process_day(name, *days)

if __name__ == "__main__":
    main(sys.argv[1:])
