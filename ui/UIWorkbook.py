from __future__ import print_function, unicode_literals
from .question_cli import make_question, make_selection, make_list

class UIWorkbook:

    def __init__(self):
        pass
    
    def select_sheet_names(self, sheets_names, workbook_name):
        separator = '= 📊 Select worksheets of ' + workbook_name + " ="
        sheets_names_list = [{'name': i, 'checked': True} for i in sheets_names]
        selected_sheets_names = make_selection("sheets","Workbook "+workbook_name+" =>", sheets_names_list, separator)
        return selected_sheets_names['sheets']
      
