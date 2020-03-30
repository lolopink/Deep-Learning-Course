'''
使用TensorFlow张量运算计算w和b，并输出结果。
已知：
x=[ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y=[ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
计算：

其中，Xi是x中索引值为i的元素；Yi是y中索引值为i的元素；n是张量中元素的个数。
(3)分别输出W和b的结果。
'''

import tensorflow as tf;

x = tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]);
y = tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]);

numpyX = x.numpy();     #得到张量x对应的数组
numpyY = y.numpy();     #得到张量y对应的数组

mol2 = sum(numpyX)*sum(numpyY);       #分子的第二个数
den2 = sum(numpyX)*sum(numpyX);       #分母的第二个数
mol1 = 0;
den1 = 0;
for i in range(0,numpyX.size):
    mol1 += numpyX[i]*numpyY[i];      #分子的第一个数
    den1 += numpyX[i]*numpyX[i];      #分母的第一个数     
mol1 = mol1*numpyX.size;     #分子的第一个数
mol = mol1-mol2;        #分子
den1 = den1*numpyX.size;     #分母的第一个数
den = den1-den2;        #分母

w = mol/den;
print("w =",w);      #题(1)的答案

b = (sum(numpyY)-w*sum(numpyX))/numpyX.size;
print("b =",b);