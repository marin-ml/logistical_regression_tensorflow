

# ###########################################################################################
# ######                Generate the Type List file for Pre-processing                  #####
# ###########################################################################################

import xlrd
import xlwt
import csv


fname_source_csv = "churn-training-aug-2016.csv"
fname_source_attr = "Attribute List.xlsx"
fname_type_xls = "Type.xls"

print "Reading Source Data file ..."
file_in = open(fname_source_csv, 'rb')
reader = csv.reader(file_in)

All_data = []
ROWS = 0
for row_data in reader:
    All_data.append(row_data)
    ROWS += 1

print "Reading Attribute List file ..."
COLS = 5
book_type = xlrd.open_workbook(fname_source_attr)
sheet_in2 = book_type.sheet_by_index(0)

book_out1 = xlwt.Workbook(encoding="utf-8")
sheet_out1 = book_out1.add_sheet("sheet1")

for j in range(COLS):
    MAX_VAL = 0
    MIN_VAL = 999999999
    list_data = []
    list_count = 0

    type = sheet_in2.cell(j, 1).value
    sheet_out1.write(j, 0, sheet_in2.cell(j, 0).value)
    sheet_out1.write(j, 1, type)

    if type == 3:
        list_data = ['']
        list_count = 1

        for i in range(ROWS - 1):
            cell_value = All_data[i + 1][j]
            comp_ind = 0
            for k in range(list_count):
                if cell_value == list_data[k]:
                   comp_ind = 1

            if comp_ind == 0 and list_count < 254:
                list_data.append(cell_value)
                list_count += 1
                sheet_out1.write(j, list_count+1, cell_value)

        sheet_out1.write(j, 2, list_count-1)

print "Generating Type List file ..."
book_out1.save(fname_type_xls)

print "Generated Type List file successfully!"
