import sys
import xlrd
import json


if len(sys.argv) < 2:
	raise Exception('Invalid args number')

filenameFullpath = sys.argv[1]
workbook = xlrd.open_workbook(filenameFullpath)
worksheet = workbook.sheet_by_index(0)
rows = worksheet.nrows
cols = worksheet.ncols
jsonArray = []
for i in range(1,rows):
	obj = {}
	for j in range(0, cols):
		label = worksheet.cell(0, j).value
		obj[label] = worksheet.cell(i, j).value
	#print json.dumps(obj)
	jsonArray.append(obj)

#print jsonArray

SEPARATOR = ''
filename = SEPARATOR.join(filenameFullpath.split('/')[-1].split('.')[0:-1])
print filename

with open('fileParse/' + filename + '.json', 'w') as f:
	json.dump(jsonArray, f)

