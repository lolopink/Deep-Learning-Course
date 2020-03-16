'''
(1) 下载波士顿数据集，读取全部506条数据，放在NumPy数组x、y中（x：属性，y：标记）。(5分)
(2) 使用全部506条数据，实现波士顿房价数据集可视化，如图1所示。(10分)
(3) 要求用户选择属性，如图2所示，根据用户的选择，输出对应属性的散点图，如图3所示。(5分)
'''

import matplotlib.pyplot as plt;
import numpy as np;
import tensorflow as tf;

#下载波士顿数据集
boston_housing = tf.keras.datasets.boston_housing;
(train_x,train_y),(test_x,test_y) = boston_housing.load_data(test_split=0);

plt.rcParams["font.sans-serif"] = "SimHei";     #设置字体为黑体

#读取全部506条数据，放在NumPy数组x、y中
x = np.array(train_x);      #所有(13个)属性的数据（506条）
y = np.array(train_y);      #所有房价平均值（506条）

titles = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT"];        #13张图表的标题
x_mins = [-20,-20,-5,-0.2,0.3,3,-20,0,-5,100,12,-100,-5];       #13张图表x轴的最小范围
x_maxs = [100,120,30,1.2,1.0,10,120,14,30,800,24,500,40];       #13张图表x轴的最大范围

plt.figure(figsize=(12,12));

#(2) 使用全部506条数据，实现波士顿房价数据集可视化
for i in range(13):
    plt.subplot(4,4,(i+1));     #划分子图
    plt.scatter(x[:,i],y,color="blue");        #绘制散点
    plt.title(str(i+1) + "." + titles[i] + " - Price");        #每个散点图的子标题
    plt.xlim(x_mins[i],x_maxs[i]);        #每个散点图x轴的范围
    plt.ylim(0,60);     #每个散点图y轴的范围
    plt.xlabel(titles[i]);      #每个散点图的x轴标签
    plt.ylabel("Price($1000's)");       #每个散点图的y轴标签

plt.tight_layout(rect=[0,0,1,0.96]);
plt.suptitle("各个属性与房价的关系");
plt.show();