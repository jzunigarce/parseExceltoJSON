import xlrd
from ValueTypeInterface import ValueTypeInterface 

class DateValue(ValueTypeInterface):
    def parse(self, value):
        return xlrd.xldate_as_datetime(value, 0).date().isoformat()
