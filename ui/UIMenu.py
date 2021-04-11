# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from pprint import pprint
from Workbook import Workbook
from .question_cli import make_question, make_selection, make_list

class UIMenu:
    def __init__(self):
        self.draw()

    def draw(self):
        print("🚀 xlsx to JSON converter")
        self.menu()

    def menu(self):
        file_path = make_question("filename", "File name")
        try:
            workbook = Workbook(file_path['filename'])
            sheets_names = workbook.list_sheet_names()
            separator = '= Select worksheets ='
            selected_sheets = make_selection("sheets", "Select sheets", sheets_names, separator)
            selected_sheets = selected_sheets['sheets']
            config_option = make_list("config_option", "Please pick a config option?", ["default", "manual"])
            print(config_option)
        except FileNotFoundError:
            pprint("An error occurred while trying to open the workbook")
            return
    
