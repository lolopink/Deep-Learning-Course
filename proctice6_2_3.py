'''
(3) 要求用户选择属性，如图2所示，根据用户的选择，输出对应属性的散点图，如图3所示。(5分)
'''

import matplotlib.pyplot as plt;
import numpy as np;
import tensorflow as tf;

#下载波士顿数据集
boston_housing = tf.keras.datasets.boston_housing;
(train_x,train_y),(test_x,test_y) = boston_housing.load_data(test_split=0);

plt.rcParams["font.sans-serif"] = "Microsoft YaHei";     #设置字体为微软雅黑

#读取全部506条数据，放在NumPy数组x、y中
x = np.array(train_x);      #所有(13个)属性的数据（506条）
y = np.array(train_y);      #所有房价平均值（506条）

titles = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT"];        #13张图表的标题
x_mins = [-20,-20,-5,-0.2,0.3,3,-20,0,-5,100,12,-100,-5];       #13张图表x轴的最小范围
x_maxs = [100,120,30,1.2,1.0,10,120,14,30,800,24,500,40];       #13张图表x轴的最大范围

plt.figure(figsize=(5,7.5));        #设置画布的大小

inputNum = input("请选择属性：");
if inputNum.isdecimal() and eval(inputNum)>=1 and eval(inputNum)<=13:       ##判断用户输入的是否是整数,且此数在范围内
    plt.scatter(x[:,eval(inputNum)-1],y,color="blue");        #绘制散点
    plt.title(inputNum + "." + titles[eval(inputNum)-1] + "-Price");        #每个散点图的子标题
    plt.xlim(x_mins[eval(inputNum)-1],x_maxs[eval(inputNum)-1]);        #每个散点图x轴的范围
    plt.ylim(0,60);     #每个散点图y轴的范围
    plt.xlabel(titles[eval(inputNum)-1]);      #每个散点图的x轴标签
    plt.ylabel("Price($1000's)");       #每个散点图的y轴标签

    #显示上面的标题
    stitle = '';
    for i in range(13):
        stitle += str(i+1) + " -- " + titles[i] + "\n";
    stitle += "请选择属性：" + inputNum;
    plt.suptitle(stitle,x=0.02,horizontalalignment="left");



    plt.tight_layout(rect=[0,0,1,0.6]);
    plt.show();
else:
    print("您输入的序号不在属性范围内！");

