
# ###########################################################################################
# #####             Predict the value with Machine Learning Coefficient file            #####
# ###########################################################################################

import xlrd
import xlwt
import func
import csv


fname_coef_xls = "coef.xls"
fname_source_csv = "churn-training-aug-2016.csv"
fname_type_xls = "Type.xls"
fname_predict = "Data_prediction.xls"

print("Reading Type List file...")
type_list = func.load_type(fname_type_xls)

print("Reading Data file...")
file_in = open(fname_source_csv, 'rb')
reader = csv.reader(file_in)


print("Standardization Data file...")
x_test = []
for row_data in reader:
    r = func.get_real(type_list, row_data)
    x_test.append(r)

print("Reading Coefficient file...")
book_in1 = xlrd.open_workbook(fname_coef_xls)
sheet_in1 = book_in1.sheet_by_index(0)
sheet_in2 = book_in1.sheet_by_index(1)

b = []
b.append(float(sheet_in2.cell(0, 0).value))
b.append(float(sheet_in2.cell(0, 1).value))

W = []
for i in range(sheet_in1.nrows):
    wcell = []
    wcell.append(float(sheet_in1.cell(i, 0).value))
    wcell.append(float(sheet_in1.cell(i, 1).value))
    W.append(wcell)

print("Predicting default value ...")
book_out = xlwt.Workbook(encoding="utf-8")
sheet_out = book_out.add_sheet("sheet")
for i in range(x_test.__len__()):
    s1 = 0
    s2 = 0
    for j in range(x_test[0].__len__()):
        if x_test[i][j] == '':
            d = 0
        else:
            d = int(x_test[i][j])
        s1 += d * W[j][0]
        s2 += d * W[j][1]

    s1 += b[0]
    s2 += b[1]
    if s1 > s2:
        sheet_out.write(i, 0, 0)
    else:
        sheet_out.write(i, 0, 1)


book_out.save(fname_predict)
print('Finished successfully')
