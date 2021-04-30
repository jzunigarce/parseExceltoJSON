# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from pprint import pprint
from Workbook import Workbook
from .question_cli import make_question, make_selection, make_list
from .UIWorkbook import UIWorkbook
import json_file
import file_helper

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
            for s in source:
                print(source)
                workbook = Workbook()
                workbook.open(s)
                sheets_names = workbook.list_sheet_names()
                
                uiWorkbook = UIWorkbook();
                selected_sheets = uiWorkbook.select_sheet_names(sheets_names)
                config_option = make_list("config_option", "Please pick a config option?", ["default", "manual"])
                worksheets = [workbook.open_sheet(sheet_name) for sheet_name in selected_sheets]
                
                for worksheet in worksheets:
                    obj_array = worksheet.parse_obj()
                    if config_option['config_option'] == 'default':
                        filename = worksheet.get_name()
                    else:
                        periodo = [val for key, val in obj_array[0].items() if "PERIODO" in key.upper()]
                        filename = str(obj_array[0]["CLAVE PLANTEL (CCT)"]) + "-" + str(obj_array[0]["CLAVE CARRERA"]) + "-" + str(obj_array[0]["GRUPO"]) + "-" + str(obj_array[0]["SEMESTRE"]) + "-" + str(obj_array[0]["CLAVE PLANTEL (CCT)"]) + "-" + str(periodo[0]) 
                        print(filename)
                    json_file.write(s, obj_array, filename) 
        except FileNotFoundError as e: 
            print("An error occurred while trying to open the workbook %s" % (e))
            return
        except Exception as e:
            print("An error ocurred %s" % (str(e)))
            return
    

