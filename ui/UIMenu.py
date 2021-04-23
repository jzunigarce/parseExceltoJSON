# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from pprint import pprint
from Workbook import Workbook
from .question_cli import make_question, make_selection, make_list
from .UIWorkbook import UIWorkbook
import json_file
class UIMenu:
    def __init__(self):
        self.draw()

    def draw(self):
        print("🔃 xlsx to JSON converter")
        self.menu()

    def menu(self):
        try:
            source = make_question("filename", "📗 File name")['filename']
            workbook = Workbook()
            workbook.open(source)
            sheets_names = workbook.list_sheet_names()
            
            uiWorkbook = UIWorkbook();
            selected_sheets = uiWorkbook.select_sheet_names(sheets_names)
            #config_option = make_list("config_option", "Please pick a config option?", ["default", "manual"])
            worksheets = [workbook.open_sheet(sheet_name) for sheet_name in selected_sheets]
            
            '''if config_option['config_option'] == 'default':
                print("default")
            else:
                print("Manual")'''
            for worksheet in worksheets:
                obj_array = worksheet.parse_obj()
                json_file.write(source, obj_array, worksheet.get_name())
                
        except FileNotFoundError:
            pprint("An error occurred while trying to open the workbook")
            return
    

