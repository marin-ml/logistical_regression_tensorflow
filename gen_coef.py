
# ###########################################################################################
# ######             Generate the Coefficient xls file from binary file                 #####
# ###########################################################################################


import xlwt
import tensorflow as tf


def xaver_init(n_inputs, n_outputs, uniform = True):
    if uniform:
        init_range = tf.sqrt(6.0 / (n_inputs + n_outputs))
        return tf.random_uniform_initializer(-init_range, init_range)

    else:
        stddev = tf.sqrt(3.0 / (n_inputs + n_outputs))
        return tf.truncated_normal_initializer(stddev=stddev)


fname_coefficient = "model_bin.ckpt"
fname_coef_xls = "coef.xls"
in_cnt = 4
out_cnt = 2

print "Configuring Model..."
x = tf.placeholder("float", [None, in_cnt])
y = tf.placeholder("float", [None, out_cnt])
W1 = tf.get_variable("W1", shape=[in_cnt, out_cnt], initializer=xaver_init(in_cnt, out_cnt))
b1 = tf.Variable(tf.zeros([2]))
activation = tf.add(tf.matmul(x, W1), b1)
t1 = tf.nn.softmax(activation)
init = tf.initialize_all_variables()
sess = tf.Session()
saver = tf.train.Saver()
sess.run(init)

print ('load learning coefficient ...')
saver.restore(sess, fname_coefficient)

ret_w = sess.run(W1)
ret_b = sess.run(b1)

book_out1 = xlwt.Workbook(encoding="utf-8")
sheet_out1 = book_out1.add_sheet("sheet1")
sheet_out2 = book_out1.add_sheet("sheet2")

for i in xrange(in_cnt):
    sheet_out1.write(i, 0, ret_w[i][0].__str__())
    sheet_out1.write(i, 1, ret_w[i][1].__str__())

sheet_out2.write(0, 0, ret_b[0].__str__())
sheet_out2.write(0, 1, ret_b[1].__str__())

book_out1.save(fname_coef_xls)
print ('Finished successfully')