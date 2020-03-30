'''
第8讲 单元作业1
使用TensorFlow张量运算计算w和b，并输出结果。
已知：
x=[ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y=[ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
计算：

其中  和  分别为x和y的均值，是x中索引值为i的元素，是y中索引值为i的元素。
(3)分别输出W和b的结果。
提示：
正确的输出结果为
w= 0.83215......
b= 10.2340.......
'''

import numpy as np;
import tensorflow as tf;

x = tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]);
y = tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]);

numpyX = x.numpy();     #得到张量x对应的数组
numpyY = y.numpy();     #得到张量y对应的数组

#求题(1)
averX = np.sum(numpyX)/numpyX.size;       #x的平均数
averY = np.sum(numpyY)/numpyY.size;       #y的平均数
mol=0;
den=0;
for i in range(0,numpyX.size):
    mol += (numpyX[i]-averX)*(numpyY[i]-averY);      #分子 
    den += (numpyX[i]-averX)*(numpyX[i]-averX);      #分母
w = mol/den;
print("w =",w);      #题(1)的答案

#求题(2)
b = averY-w*averX;      
print("b =",b);        #题(2)的答案