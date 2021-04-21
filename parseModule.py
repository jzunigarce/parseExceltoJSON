import xlrd
from DateValue import DateValue
from NumberValue import NumberValue
from StrValue import StrValue


def parse_value(cell):
    if cell.ctype is xlrd.XL_CELL_DATE:
        return DateValue().parse(cell.value)
    elif cell.ctype is xlrd.XL_CELL_NUMBER:
        return NumberValue().parse(cell.value)
    else:
        return StrValue().parse(cell.value)
