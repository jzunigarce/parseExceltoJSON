# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from pprint import pprint
from Workbook import Workbook
from .question_cli import make_question, make_selection, make_list
from .UIWorkbook import UIWorkbook
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
                selected_sheets = uiWorkbook.select_sheet_names(sheets_names)
                worksheets = [workbook.open_sheet(sheet_name) for sheet_name in selected_sheets]
                
                for worksheet in worksheets:
                    if config_option['config_option'] == 'default':
                        filename = worksheet.get_name()
                    else:
                        periodo_column_name = [val for val in worksheet.list_columns_name() if "PERIODO" in val.upper()]
                        new_columns_names = []
                        new_columns_names.append((periodo_column_name[0], "PERIODO"))
                        worksheet.change_column_name(new_columns_names)
                        columns_key = ["CLAVE PLANTEL (CCT)", "CLAVE CARRERA", "GRUPO", "SEMESTRE", "CLAVE PLANTEL (CCT)", "PERIODO"]
                        separator_filename = "-"
                        filename = str(count) + "-" + separator_filename.join([str(worksheet.get_cell(1, worksheet.get_index_column_name(col_key))) for col_key in columns_key])
                        count += 1
                    obj_array = worksheet.parse_obj()
                    json_file.write(s, obj_array, filename) 
        except FileNotFoundError as e: 
            print("An error occurred while trying to open the workbook %s" % (e))
            return
        except Exception as e:
            print(traceback.format_exc())
            return
    

