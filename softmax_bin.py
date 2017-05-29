
# ###########################################################################################
# ######         Machine Learning Stage using logistical Regression Method              #####
# ###########################################################################################

import tensorflow as tf
import csv


fname_training = "Training.csv"
fname_training_y = "y_label.csv"
fname_coefficient = "model_bin.ckpt"
in_cnt = 4
out_cnt = 2
learning_rate = 0.00001


def xaver_init(n_inputs, n_outputs, uniform = True):
    if uniform:
        init_range = tf.sqrt(6.0/ (n_inputs + n_outputs))
        return tf.random_uniform_initializer(-init_range, init_range)

    else:
        stddev = tf.sqrt(3.0 / (n_inputs + n_outputs))
        return tf.truncated_normal_initializer(stddev=stddev)


def acc(d1, d2):
    cnt = 0
    for i in range(d1.__len__()):
        if d1[i] == d2[i]:
            cnt += 1

    return float(cnt)/d1.__len__()


def sel_max(data):
    ret_ind = []
    for i in range(data.__len__()):
        if data[i][0] == 1:
            ret_ind.append(0)
        else:
            ret_ind.append(1)

    return ret_ind


x_training = []
y_training = []

print("Loading training data ...")
file_in_y = open(fname_training_y, 'rb')
reader_y = csv.reader(file_in_y)
y_data = []
for row_data in reader_y:
    y_data.append(row_data[0])
    if row_data[0] == '0':
        y_training.append([1, 0])
    elif row_data[0] == '1':
        y_training.append([0, 1])

file_in = open(fname_training, 'rb')
reader = csv.reader(file_in)
ROWS = 0
for row_data in reader:
    if y_data[ROWS] != '2':
        x_training.append(row_data)
    ROWS += 1

# Configuration Learning Model
x = tf.placeholder("float", [None, in_cnt])
y = tf.placeholder("float", [None, out_cnt])

W1 = tf.get_variable("W1", shape=[in_cnt, out_cnt], initializer=xaver_init(in_cnt, out_cnt))
b1 = tf.Variable(tf.zeros([out_cnt]))
activation = tf.add(tf.matmul(x, W1), b1)
t1 = tf.nn.softmax(activation)

# Minimize error using cross entropy
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(activation, y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Initializing the variables
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
saver = tf.train.Saver()

print('load learning coefficient ...')
saver.restore(sess, fname_coefficient)

# Training cycle
for step in range(20000):
    sess.run(optimizer, feed_dict={x: x_training, y: y_training})
    if step % 50 == 0:
        ret = sess.run(t1, feed_dict={x: x_training})
        ret1 = sel_max(ret)
        acc1 = acc(ret1, sel_max(y_training))*100

        print(step, sess.run(cost, feed_dict={x: x_training, y: y_training}), acc1)

        saver.save(sess, fname_coefficient)

print("Optimization Finished!")

