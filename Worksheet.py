import xlrd
from parseModule import parse_value

class Worksheet:

    def __init__(self, sheet):
        self.sheet = sheet
        self.columns_names = [sheet.cell(0, col).value for col in range(self.sheet.ncols)]
        self.rows = self.sheet.nrows

    def list_columns_name(self):
        return self.columns_names

    def get_name(self):
        return self.sheet.name

    def parse_obj(self):
        cols = len(self.columns_names)
        obj_array = []
        for i in range(1, self.rows):
            obj = {}
            for j in range(cols):
                label = self.columns_names[j]
                obj[label] = parse_value(self.sheet.cell(i, j))
            obj_array.append(obj)
        return obj_array

    def change_column_name(self, columns):
        for col in columns:
            #i = self.columns_names.index(col[0])
            i = self.get_index_column_name(col[0])
            self.columns_names[i] = col[1]

    def get_cell(self, i, j):
        return self.sheet.cell_value(i, j)

    def get_index_column_name(self, key):
        return self.columns_names.index(key)
