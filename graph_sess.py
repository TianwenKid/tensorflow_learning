# -*- coding: UTF-8 -*-

# 引入tensorflow
import tensorflow as tf


# 创建两个常亮 Tensor
const1 = tf.constant([[2,2]])
const2 = tf.constant([[4],[4]])

multiple = tf.matmul(const1, const2)

# 尝试用print输出multiple的值
print(multiple)


# 创建Session对象
sess = tf.Session()

# 用Session的run方法来实际运行该矩阵乘法操作
result = sess.run(multiple)

# 用print打印
print(result)

# 关闭以用完的Session
sess.close()

# 第二种方法来创建和关闭Session

with tf.Session() as sess:
    result2 = sess.run(multiple)
    print('Multiple的结果是 %s' % result2)
