#<font color=#5F9EA0>Abstract</font>
这是计算物理课程的第三次作业，分为两个小问题。
#Problems and Solutions
Level 2
　　用“#”打印任意次序的字符串（比如姓名），并让其水平移动起来。
Solution
　　2-1
　　这里想到把所有常用字符的“#”图形（12*8）用列表预先输入，然后定义一个字典，其键为字符常量，对应值为字符的“#”列表。（这里的“#”列表的预设参考了[ShixingWang](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Codes/Exercise2_level3_new.py)的格式，十分感谢！）
　　预设完毕后可以利用三层for循环来输出目标字符串，这三层for循环分别是控制字符串的遍历，字典键值的遍历以及输出格式（12行预设的“#”）。
　　若要使该字符串水平移动起来，只需设置一个专门输出空格的列表，其长度由一个for循环控制，在这个循环中，每次都将空格列表加在字符串列表之前，然后利用下面代码来实现帧输出：
```python
import os
os.system('cls')
```
　　其中帧数可由下面的代码控制：
```python
import time
time.sleep()
```

　　由于技术上的差距，自己暂时还未想出自动换行的方法，所以字符的长度和水平移动的距离都还有限。实现效果如图：

![level_2-1](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_2-1.gif)

[程序2-1](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_2-1.py)

　　2-2
　　自动换行的功能可以由[ShixingWang](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Codes/Exercise2_level3_new.py)的代码实现。由于学长的输出思路和我完全不同，故将其方法移植到我的程序中难度比较大......目前还在观摩中......效果如图:

![level_2-2](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_2-2.gif)

[程序2-2](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_2-2.py)


Level 3
　　在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）
Solution
　　3-1
 　　为方便起见，仍取Level2中“#”字符串做旋转（其实是平移，中心转动真的不会......）,在屏幕上的旋转方式可以自定义（取决于程序中的变量k），此处k设为一个余弦运动。此处字符串预设部分仍采用了Level2的部分程序，平移部分则参考了[HenryWang96](https://github.com/HenryWang96/compuational_physics_N2014301610094/blob/master/TASK-3/name.py)的部分程序，十分感谢！实现效果如图：

![level_3-1](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_3-1.gif)

[程序3-1](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_3-1.py)


　　3-2
　　另外，题目要求用字符作画，查阅资料后发现通过灰度识别可以将已有的图像文件用70个映射到256灰度的字符输出，实测该方法后发现实际效果取决于图像的长宽比，实现效果如下：

![level_3-2](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_3-2.png)

[程序3-2](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_3-2.py)

#Code

[Level2-1](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_2-1.py)

[Level2-2](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_2-2.py)

[Level3-1](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_3-1.py)

[Level3-2](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_03-All-levels/level_3-2.py)
　　　　　　　　　　　　　
#Conclusion
　　通过编写Python小程序解决了打印字符字、字符画的问题，复习了Python的语法规则，熟悉了Python中列表、字典、函数的使用，为以后的学习奠定了基础。

#Difficulty
　　自动换行、中心旋转待解决。
　　
#Thanks and References

[ShixingWang](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Codes/Exercise2_level3_new.py)

[HenryWang96](https://github.com/HenryWang96/compuational_physics_N2014301610094/blob/master/TASK-3/name.py)

[Python字符画](http://blog.csdn.net/sparroww/article/details/50396840)
               
  ***
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　杜琛，2016/9/25
