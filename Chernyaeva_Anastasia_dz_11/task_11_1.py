import re

RE_DATE = re.compile(r'^(\d{2})(?:-)(\d{2})(?:-)(\d{4})$')


class Date:
    date_value = '01-01-1970'

    def __init__(self, datestring):
        self.__class__.date_value = self.__class__.check_date_values(datestring)

    @classmethod
    def get_date_as_numbers(cls):
        datestring = cls.date_value
        findall_result = RE_DATE.search(datestring).groups()
        return [int(val) for val in findall_result]

    @staticmethod
    def check_date_values(datestring):
        if type(datestring) != str:
            raise TypeError('date must be provided as string')
        if not RE_DATE.match(datestring):
            raise ValueError('Date must be provided in DD-MM-YYYY format')
        day, month, year = RE_DATE.search(datestring).groups()
        if int(month) < 1 or int(month) > 12:
            raise ValueError(f'Month value {month} of out of range')
        if int(month) in [1, 3, 5, 7, 8, 10, 12]:
            maxday = 31
        elif int(month) in [4, 6, 9, 11]:
            maxday = 30
        else:
            maxday = int(int(year) % 4 == 0) + 28
        if int(day) < 1 or int(day) > maxday:
            raise ValueError(f'Day value {day} of out of range')
        return datestring


a = Date('02-03-2004')
print(Date.get_date_as_numbers())
Date.check_date_values('28-02-2022')
Date.check_date_values('29-02-2022')
