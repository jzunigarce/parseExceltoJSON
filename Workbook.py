import xlrd

class Workbook:

    def __init__(self, file_path):
        self.book = self.open_workbook(file_path) 

    def open_workbook(self, file_path):
        return xlrd.open_workbook(file_path)

    def list_sheet_names(self):
        list_names = self.book.sheet_names()
        print(list_names)
        return [{'name': i, 'checked': True} for i in self.book.sheet_names()]
