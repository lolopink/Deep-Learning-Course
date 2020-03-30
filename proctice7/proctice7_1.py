'''
下载lena.tiff图像（见7.2小节课件），将R、G、B三通道分离，采用灰度图表示颜色的亮度，并分别对各个通道按要求进行处理，结果显示在如图1所示的画布中
要求：
(1)将R通道的图像缩小为50×50，显示在子图1中，子标题为:“R-缩放”，字体大小为14；
(2)将G通道的图像先水平镜像，再顺时针旋转90度，显示在子图2中，子标题为:“G-镜像+旋转”，字体大小为14，并显示坐标轴；
(3)对B通道的图像进行裁剪，裁剪位置：左上角(0, 0) 右下角(150, 150)，显示在子图3中，子标题为:“B-裁剪”，字体大小为14；
(4)将原始的R、G、B通道的图像合并，显示在子图4中，子标题显示图像的色彩模式，字体大小为14；
(5)将要求(4)的处理结果保存为PNG格式的图片，路径为当前工作目录，文件名为“test.png”，如图2所示；
(6)将以上生成的4幅图像显示在2×2的画布中，全局标题为“图像基本操作”，标题字体大小为20，颜色为蓝色。 
'''

import matplotlib.pyplot as plt;
from PIL import Image;      #导入Pillow图像处理库的PIL.image模块


plt.rcParams["font.sans-serif"] = "SimHei";     #设置字体为黑体

img = Image.open("lena.tiff");      #打开图像
img_r,img_g,img_b = img.split();        #将彩色图像分离为R,G,B三个颜色通道

#划分子图
#子图1
plt.subplot(221); 
plt.axis("off");        #不显示表的坐标轴
img_small = img_r.resize((50,50));      #将R通道的图像缩小为50×50
plt.imshow(img_small,cmap="gray");      #在表中插入图片img_small，cmap="gray"表示采用灰度图表示颜色的亮度
plt.title("R-缩放",fontsize=14);        #子图1的子标题
#子图2
plt.subplot(222); 
plt.title("G-镜像+旋转",fontsize=14);       #子图2的子标题
img_small = img_g.resize((250,250));       #将G通道的图像缩小到250x250
plt.xlim(0,250);        #限定子图2的x轴的范围
plt.ylim(0,250);        #限定子图2的y轴的范围
img_flr = img_small.transpose(Image.FLIP_LEFT_RIGHT);       #将缩小后的G通道的图像先水平镜像(水平翻转)
img_r270 = img_small.transpose(Image.ROTATE_270);       #再将缩小后的G通道的图像顺时针旋转90度(逆时针旋转270度)
plt.imshow(img_r270,cmap="gray");       #在表中插入图片img_r270，cmap="gray"表示采用灰度图表示颜色的亮度
#子图3
plt.subplot(223);
plt.title("B-裁剪",fontsize=14);        #子图3的子标题  
plt.axis("off");        #不显示表的坐标轴
img_small = img_b.resize((250,250));       #将B通道的图像缩小到250x250
img_region = img_small.crop((0,0,150,150));     #对缩小后的B通道的图像进行裁剪，裁剪位置：左上角(0, 0) 右下角(150, 150)
plt.imshow(img_region,cmap="gray");      #在表中插入图片img_region，cmap="gray"表示采用灰度图表示颜色的亮度
#子图4
plt.subplot(224);
plt.title("RGB",fontsize=14);       #子图4的子标题 
plt.axis("off");        #不显示表的坐标轴
img_rgb = Image.merge("RGB",[img_r,img_g,img_b]);       #将所有通道合并，得到RGB彩色图像
plt.imshow(img_rgb);        #显示img_rgb图像

#将要求(4)的处理结果(此时的img_rgb)保存为PNG格式的图片，路径为当前工作目录，文件名为“test.png”
img_rgb.save("test.png");

plt.tight_layout(rect=[0,0,1,0.95]);        #自动调整子图，并规范子图区域   
plt.suptitle("图像基本操作",color="b",fontsize=20);     #全局标题
plt.show();