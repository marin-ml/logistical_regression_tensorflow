
# ###########################################################################################
# ######         Pre-processing stage (Convert the raw data to Training data            #####
# ###########################################################################################


import func
import csv


fname_source_csv = "churn-training-aug-2016.csv"
fname_training = "Training.csv"
fname_type_xls = "Type.xls"


def conv_data(f_in, f_out, type_data):

    file_in = open(f_in, 'rb')
    reader = csv.reader(file_in)
    file_out = open(f_out, 'wb')
    writer = csv.writer(file_out)

    i = 0
    w_data = []
    for row_data in reader:
        if i % 10 == 0:
            print i
        out_data = func.get_real(type_data, row_data)
        w_data.append(out_data)
        i += 1

    writer.writerows(w_data)
    file_in.close()
    file_out.close()


print "Reading Type List file ..."
type_list = func.load_type(fname_type_xls)

print "Converting Training data 1 file ..."
conv_data(fname_source_csv, fname_training, type_list)
