import os
import sys
import xlrd
import json

def full_path(source):
	filename = os.path.splitext(os.path.basename(source))[0]
	fullpath =  os.path.dirname(os.path.abspath(source))
	filenameExt = 'json'
	return os.path.join(fullpath, filename + "." + filenameExt)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		raise Exception('Invalid args number')

	source = sys.argv[1]
	workbook = xlrd.open_workbook(source)
	worksheet = workbook.sheet_by_index(0)
	rows = worksheet.nrows
	cols = worksheet.ncols
	jsonArray = []
	for i in range(1,rows):
		obj = {}
		for j in range(0, cols):
			label = worksheet.cell(0, j).value
			obj[label] = worksheet.cell(i, j).value
		jsonArray.append(obj)



	fullpath = full_path(source)

	with open(fullpath, 'w') as f:
		json.dump(jsonArray, f)
