# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from pprint import pprint
from Workbook import Workbook
from .question_cli import make_question, make_selection, make_list
from .UIWorkbook import UIWorkbook
from .UIWorksheet import UIWorksheet
import json_file
import file_helper
import traceback

class UIMenu:
    def __init__(self):
        self.draw()

    def draw(self):
        print("🔃 xlsx to JSON converter")
        self.menu()

    def menu(self):
        try:
            source = make_question("filename", "📗 File name")['filename']
            source = source.rstrip().replace("\\", "")
            source = file_helper.list_xlsx(source)
            config_option = make_list("config_option", "Please pick a config option?", ["default", "manual"])
            count = 1
            for s in source:
                workbook = Workbook()
                workbook.open(s)
                sheets_names = workbook.list_sheet_names()
                
                uiWorkbook = UIWorkbook();
                selected_sheets = uiWorkbook.select_sheet_names(sheets_names, s)
                worksheets = [workbook.open_sheet(sheet_name) for sheet_name in selected_sheets]
                
                for worksheet in worksheets:
                    if config_option['config_option'] == 'default':
                        filename = worksheet.get_name()
                    else:
                        uiWorksheet = UIWorksheet()
                        selected_columns = uiWorksheet.select_columns_names(worksheet.list_columns(), worksheet.get_name())
                        worksheet.filter_columns(selected_columns)
                        filename = uiWorksheet.set_name() if uiWorksheet.set_name() else worksheet.get_name()

                    obj_array = worksheet.parse_obj()
                    json_file.write(s, obj_array, filename) 
        except FileNotFoundError as e: 
            print("An error occurred while trying to open the workbook %s" % (e))
            return
        except Exception as e:
            print(traceback.format_exc())
            return
    

