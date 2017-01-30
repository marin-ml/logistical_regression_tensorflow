
import csv

file_in1 = open("churn-training-aug-2016.csv", 'rb')
reader1 = csv.reader(file_in1)

All_data1 = []
ROWS1 = 0
for row_data in reader1:
    All_data1.append(row_data)
    ROWS1 += 1

file_in2 = open("extensions_status.csv", 'rb')
reader2 = csv.reader(file_in2)

All_data2 = []
ROWS2 = 0
for row_data in reader2:
    All_data2.append(row_data)
    ROWS2 += 1

file_out = open("y_label.csv", 'wb')
writer = csv.writer(file_out)

w_data = []
for i in xrange(ROWS1):
    ext_data = All_data1[i][0].strip()
    s = '2'
    for j in xrange(ROWS2):
        s2 = All_data2[j][1]
        if ext_data == s2:
            s = All_data2[j][2]
    w_data.append(s)
writer.writerows(w_data)
