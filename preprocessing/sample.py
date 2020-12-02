import xlrd

ds_file = "DS_questions.xlsx"

#opening a xlsx workbook
wb = xlrd.open_workbook(ds_file)

#number of sheets in the excel file
sheetNums = wb.nsheets
print(sheetNums)

#accessing the first sheet
sheet = wb.sheet_by_index(0)  #i for ith sheet

#rows and columns in the sheet
row = sheet.nrows
column = sheet.ncols

#accessing the value of the cell
textValue = sheet.cell_value(row-1,column-1) #0 based index

for i in range(sheetNums):
	sheet = wb.sheet_by_index(i)
	for j in range(sheet.ncols):
		print(sheet.cell_value(0,j))