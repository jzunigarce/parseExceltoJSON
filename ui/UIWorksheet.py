from __future__ import print_function, unicode_literals
from .question_cli import make_question, make_selection, make_list

class UIWorksheet:

    def __init__(self):
        pass
    
    def select_columns_names(self, columns_names, worksheet_name):
        separator = '= 📖 Select columns of ' + worksheet_name + " ="
        columns_names_list = [{'name': i, 'checked': True} for i in columns_names]
        selected_columns_names = make_selection("columns","Worksheet "+worksheet_name+" =>", columns_names_list, separator)
        return selected_columns_names['columns']

    def set_name(self):
       return make_question("filename", "📖 Name for sheet(enter for default)")['filename']
