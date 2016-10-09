#Abstract
这是计算物理课程的第四次练习，也是我的第一个Python物理数值计算程序，包含一个常微分问题和相应的图解（即Chapter1 Exercise 1.5）。

#Background
###Chapter1-Exercise 1.5

>Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are

>　　　　　　　　　　　　　　　　　　![decay equation](http://latex.codecogs.com/gif.latex?\\frac{dN_A}{dt}=\\frac{N_B}{\\tau}-\\frac{N_A}{\\tau})　,

>　　　　　　　　　　　　　　　　　　![decay equation](http://latex.codecogs.com/gif.latex?\\frac{dN_B}{dt}=\\frac{N_A}{\\tau}-\\frac{N_B}{\\tau})　,

>where for simplicity we have assumed that the two types of decay are characterized by the same time constant, 
![tau](http://latex.codecogs.com/gif.latex?\\tau)
. Solve this system of equation for the numbers of nuclei, 
![NA](http://latex.codecogs.com/gif.latex?\N_A)
and 
![NB](http://latex.codecogs.com/gif.latex?\N_B)
, as functions of time. Consider different initial conditions, such as 
![NA](http://latex.codecogs.com/gif.latex?\N_A)
=100, 
![NB](http://latex.codecogs.com/gif.latex?\N_B)
=0, etc, and take 
![tau](http://latex.codecogs.com/gif.latex?\\tau)
=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which 
![NA](http://latex.codecogs.com/gif.latex?\N_A)
and 
![NB](http://latex.codecogs.com/gif.latex?\N_B)
are constant. In such a steady state, the time derivatives 
![dNA/dt](http://latex.codecogs.com/gif.latex?\{dN_A}/{dt}) and ![dNB/dt](http://latex.codecogs.com/gif.latex?\{dN_B}/{dt}) should vanish.

这个问题是课堂上的例题Uranium Decay的升级版，涉及到两种不同的原子核的衰变，两种原子核各有几率衰变成另一种核，因此它们的衰变规律将由两个互相耦合的一阶线性常微分方程描述。

#Thinking
由题可知问题归结为一个一阶常微分方程组，这与Uranium Decay没有本质区别，可以用欧拉法（Euler method）求得其数值解，并用图像表示。这就是解决整个问题的大致思路。

#Calculation
计算部分则主要是欧拉法的使用：
一般地，以t=0为中心对在
![](http://latex.codecogs.com/gif.latex?\t=\\Delta t)
时的原子核数目作泰勒展开有：

![Taylor expansion](http://latex.codecogs.com/gif.latex?\N(\\Delta t)=N(0)+\\frac{dN}{dt}\\Delta t+\\frac12 \\frac{d^2N}{dt^2}(\\Delta t)^2+\\cdots)

取其一阶展开式作为
![](http://latex.codecogs.com/gif.latex?\N(\\Delta t))
的近似，即：

![Taylor approx](http://latex.codecogs.com/gif.latex?\N(\\Delta t)=N(0)+\\frac{dN}{dt}\\Delta t)

这个近似可以简便地由计算机得到数值解。而对于本题，结合一阶常微分方程组，代入原子核质子数目的一阶泰勒近似，有：(取
![tau](http://latex.codecogs.com/gif.latex?\\tau)
=1s）

![Taylor approx](http://latex.codecogs.com/gif.latex?\N_A(t+\\Delta t)=N_A(t)+(\\frac{N_B(t)}{\\tau _B}-\\frac{N_A(t)}{\\tau _A})\\Delta t)

![Taylor approx](http://latex.codecogs.com/gif.latex?\N_B(t+\\Delta t)=N_B(t)+(\\frac{N_A(t)}{\\tau _A}-\\frac{N_B(t)}{\\tau _B})\\Delta t)

由此，对于给定初始的条件，我们可以得到
![NA](http://latex.codecogs.com/gif.latex?\N_A)
和
![NB](http://latex.codecogs.com/gif.latex?\N_B)
在任何时候的值，通过
![](http://latex.codecogs.com/gif.latex?\N(\\Delta t))
步长的每一步逼近不断得到数值解直到解出给定时间的
![NAt](http://latex.codecogs.com/gif.latex?\N_A(t))
和
![NBt](http://latex.codecogs.com/gif.latex?\N_B(t))
。
此方法即为欧拉法。（此处参考了老师课上的例题和[wuyuqiao](https://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/Chapter1/Homework%20of%20Chapter%201.md)的分析，十分感谢！）

#Solution
通过以上分析，我们可以着手用Python程序实现对两种原子核衰变的数值模拟。
[代码在这](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/1.5-Decay%20problem%20with%20two%20types%20of%20nuclei.py)
###1.结果

由题意，我们可以将两种原子核的衰变时间常数均设为1s，即![time constant](http://latex.codecogs.com/gif.latex?\\\tau _A=\\tau _B=1s),这种情形下我们可以得到如下图所示的结果:（为使图像清晰易懂，取时间步长为0.1s，欧拉法循环步数为100，A，B初始核质子数可自定义）

![1.5-1](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-1.png)

###2.不同衰变时间常数的结果

实际中情形并不一定尽如1中结果，所以我在此设定
![time constant](http://latex.codecogs.com/gif.latex?\\\tau _A)
和
![time constant](http://latex.codecogs.com/gif.latex?\\\tau _B)
可以不相等
且可以自行设定取值，以便进行更全面的数值模拟。示例性的结果如下：（仍取时间步长为0.1s，欧拉法循环步数为100，A，B初始核质子数可自定义）

![1.5-2](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-2.png)

![1.5-3](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-3.png)



（这里的不同衰变时间常数的思考感谢[chenfeng2013301020145](https://www.zybuluo.com/355073677/note/318129)的启发！）

###3.欧拉法模拟数值解和真实解之间的误差
根据欧拉法的数学推导，我们知道欧拉法得出的解是泰勒展开的一阶近似，因此存在精度问题。所以我们想要至少直观地发现误差的存在，并且初步探讨影响精度的因素。

首先，我们应推导出
![NAt](http://latex.codecogs.com/gif.latex?\N_A(t))
和
![NBt](http://latex.codecogs.com/gif.latex?\N_B(t))
的解析解。由题给出的一阶常微分方程组和初始条件：

![decay equation](http://latex.codecogs.com/gif.latex?\\frac{dN_A}{dt}=\\frac{N_B}{\\tau}-\\frac{N_A}{\\tau})

![decay equation](http://latex.codecogs.com/gif.latex?\\frac{dN_B}{dt}=\\frac{N_A}{\\tau}-\\frac{N_B}{\\tau})

![decay equation](http://latex.codecogs.com/gif.latex?\N_A(0)=N_{A_0})

![decay equation](http://latex.codecogs.com/gif.latex?\N_B(0)=N_{B_0})

可解出解析解：

　　　![NA(t)](http://latex.codecogs.com/gif.latex?\N_A(t)= \\frac{(N_{A_0}+N_{B_0})\\tau_A}{\\tau_A+\\tau_B}+\\frac{-N_{B_0}\\tau_A+N_{A_0}\\tau_B}{\\tau_A+\\tau_B}e^{-(\\frac{1}{\\tau_A}+\\frac{1}{\\tau_B})t})

　　　![NB(t)](http://latex.codecogs.com/gif.latex?\N_B(t)= \\frac{(N_{A_0}+N_{B_0})\\tau_B}{\\tau_A+\\tau_B}+\\frac{N_{B_0}\\tau_A-N_{A_0}\\tau_B}{\\tau_A+\\tau_B}e^{-(\\frac{1}{\\tau_A}+\\frac{1}{\\tau_B})t})

（此处感谢[ShixingWang](https://www.zybuluo.com/ShixingWang/note/321753)的推导结果！）

将解析解的结果和欧拉法得出的数值解的结果打印到同一屏幕，可得到非常直观的误差。示例性的结果如下：（为使图像清晰易懂，解析解用光滑曲线表示，数值解用点状线表示，欧拉法循环步数为100，A，B初始核质子数分别为100，0）

![1.5-4](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-4.png)

![1.5-5](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-5.png)

![1.5-6](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-6.png)

![1.5-8](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-8.png)

![1.5-9](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-9.png)

![1.5-10](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/figures/chapter1-1.5-10.png)

由此可见，时间步长的取值对欧拉法的精度的影响非常大，时间步长取得越小，欧拉法的精度越高！

#Code

[Decay problem with two types of nuclei](https://github.com/Cvke/compuational_physics_N2014302580257/blob/master/Exercise_04-Chapter-1-problem-1.5-The-decay-of-two-kinds-of-particles/1.5-Decay%20problem%20with%20two%20types%20of%20nuclei.py)

#Conclusion

通过这次的练习，进一步熟练了Python的编程，解决了Python的第一个数值计算问题，较熟练地掌握了使用Python程序进行数值模拟的简单方法，并且掌握了用matplotlib作图的基本技能。对两种原子核的交互衰变机制有了认识。

#Thanks and Reference

[chenfeng2013301020145](https://www.zybuluo.com/355073677/note/318129)

[ShixingWang](https://www.zybuluo.com/ShixingWang/note/321753)

[wuyuqiao](https://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/Chapter1/Homework%20of%20Chapter%201.md)

[NumPy-快速处理数据](http://old.sebug.net/paper/books/scipydoc/numpy_intro.html)

[Matplotlib 教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)

***
杜琛
10/9,2016
