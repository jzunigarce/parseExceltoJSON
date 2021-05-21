import xlrd
from Worksheet import Worksheet

class Workbook:

    def __init__(self):
        self.book = None

    def open(self, file_path):
        self.book = xlrd.open_workbook(file_path)

    def list_sheet_names(self):
        return self.book.sheet_names()

    def open_sheet(self, name):
        return Worksheet(self.book.sheet_by_name(name))

    def get_name(self):
        return self.book.Name
