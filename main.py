"""
Convert excel in json
 Params:
 - python file
 - fullpath from file xlsx
 optionals:
 - number of sheet
 - index of columns separated by ,
 - optional filename(by default is the current filename)
 - If you want to pass an alternative name but column indexes will not be specified pass -1
"""

import os
import sys
import json
import xlrd
import datetime
from parseModule import parseValue

def full_path(source, filename):
    if filename is None:
        filename = os.path.splitext(os.path.basename(source))[0]
    fullpath = os.path.dirname(os.path.abspath(source))
    filenameExt = 'json'
    return os.path.join(fullpath, filename + "." + filenameExt)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Invalid args number')
    
    source = sys.argv[1]
    sheet = int(sys.argv[2]) if len(sys.argv) >= 3 else 0
    selectedColumns = sys.argv[3].split(',') if len(sys.argv) >= 4 and sys.argv[3] != '-1' else []
    filename = sys.argv[4] if len(sys.argv) >= 5 else None
        
    workbook = xlrd.open_workbook(source)
    worksheet = workbook.sheet_by_index(sheet)
    rows = worksheet.nrows
    if len(selectedColumns) == 0:
        numCols = worksheet.ncols
        cols = list(range(numCols))
    else:
        cols = [int(i) for i in selectedColumns]
    jsonArray = []
    dateFormat = "%Y-%m-%d"
    for i in range(1, rows):
        obj = {}
        for j in range(len(cols)):
            label = worksheet.cell(0, cols[j]).value
            obj[label] = parseValue(worksheet.cell(i, cols[j]))
        jsonArray.append(obj)

    fullpath = full_path(source, filename)
    with open(fullpath, 'w', encoding='utf8') as f: 
        json.dump(jsonArray, f, ensure_ascii=False, separators=(',', ': '), indent=4)
