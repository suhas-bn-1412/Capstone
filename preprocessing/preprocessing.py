"""
for every row
	take text of the question
	go through all steps of pre processing
	final text = pre processed
	store final text in new file
	copy values of all other columns
"""

import xlrd
import xlwt

ds_file = "DS_questions.xlsx"

wb = xlrd.open_workbook(ds_file)
sheetNums = wb.nsheets

newWB = xlwt.Workbook()

for i in range(sheetNums):
	sheet = wb.sheet_by_index(i)
	sheetName = "Sheet" + str(i)
	newSheet = newWB.add_sheet(sheetName)
	for row in range(sheet.nrows):
		question = sheet.cell_value(row, 1)
		marks = sheet.cell_value(row, 2)
		btValue = sheet.cell_value(row, 3)

		ppQuestion = "pre processed question" #To DO

		newSheet.write(row, 0, ppQuestion)
		newSheet.write(row, 1, marks)
		newSheet.write(row, 2, btValue)

newWB.save("processed_ds.xlsx")