'''
按下列要求完成程序，随机显示MNIST数据集中的样本，效果如图1所示。
要求：
(1)下载手写数字数据集，读取训练集和测试集数据，放在NumPy数组train_x、train_y、test_x、test_y中；
（train_x：训练集图像，train_y：训练集标签，test_x：测试集图像，test_y：测试集标签）
(2)随机从所有测试集数据中显示16幅数字图像；
(3)16幅图像按照4×4方式排列在一张画布中，每幅图像的子标题为该图像的标签值，
字体大小为14，全局标题为“MNIST测试集样本”，字体大小为20，颜色为红色。
'''

import tensorflow as tf;
import numpy as np;
import matplotlib.pyplot as plt;

plt.rcParams["font.sans-serif"] = "SimHei";     #设置字体为黑体

#下载MNIST数据集
mnist = tf.keras.datasets.mnist;
(train_x,train_y),(test_x,test_y) = mnist.load_data();      #60000条训练数据，10000条测试数据 

for i in range(16):
    num = np.random.randint(1,10000);       #索引值随机从0-9999中产生
    plt.subplot(4,4,i+1);       #划分子图4*4
    plt.axis("off");        #不显示表的坐标轴
    plt.imshow(test_x[num],cmap="gray");        #随机从所有测试集数据中显示16幅数字图像
    titleName = "标签值:" + str(test_y[num]);       #拼接子标题
    plt.title(titleName,fontsize=14);        #每幅图像的子标题为该图像的标签值

plt.tight_layout(rect=[0,0,1,0.94]);        #自动调整子图，并规范子图区域
plt.suptitle("MNIST测试集样本",color="r",fontsize=20);        #全局标题
plt.show();
