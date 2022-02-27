"The Employee class"

from interface_employee import IEmployee
from day import Day


class Employee(IEmployee):
    "Class Employee"
    @staticmethod
    def process_day(name: str, *args: Day):
        "Method use to calculate houw much ACME have to pay to anemployee"

        total_to_pay: int = 0
        for day in args:
            total_to_pay += day.get_prices()

        print(f"The amount to pay {name} is: {int(total_to_pay)} USD")
