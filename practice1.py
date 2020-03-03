'''
利用 Python 完成一元二次方程 ax²+bx+c=0 的求解，要求程序输入任意    
a,b,c的值后，程序能判断输出有解或无解，有解的话，输出x的解为多少。
'''
import math;

a = input("请输入a的值：");
b = input("请输入b的值：");
c = input("请输入c的值：");
if eval(a)==0:
    if eval(b)==0:
        print("方程无解。");
    else:
        x = eval(b)/eval(c)
        print("方程有解，x的解为：{:.2f}".format(x));
else:
    if math.pow(eval(b),2) > 4*eval(a)*eval(c) or math.pow(eval(b),2) == 4*eval(a)*eval(c):
        x1 = (-eval(b)+math.sqrt(math.pow(eval(b),2)-4*eval(a)*eval(c)))/(2*eval(a));
        x2 = (-eval(b)-math.sqrt(math.pow(eval(b),2)-4*eval(a)*eval(c)))/(2*eval(a));
        if x1==x2:
            print("方程有解，x的解为：{:.2f}".format(x1));
        else:
            print("方程有解，x的解为：{:.2f}和{:.2f}".format(x1,x2));
            # print("方程有解，x的解为：%f和%f"%(x1,x2));
    else:
        print("方程无解。");

