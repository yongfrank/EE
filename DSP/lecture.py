'''
Author: Frank Chu
Date: 2023-02-20 23:51:56
LastEditors: Frank Chu
LastEditTime: 2023-02-27 18:52:58
FilePath: /EE/DSP/lecture.py
Description: 
【一个视频教你理解两种数字滤波器，学数字信号处理必看】 https://www.bilibili.com/video/BV1Gb4y1b78C/?share_source=copy_web&vd_source=bf4952280cde801b178268abc99a7047

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''

import numpy as np

from matplotlib import pyplot as plt
x = np.linspace(1, 100, 100)
y = 0.01 * x ** 2 - x + 123
print(len(x))
y = y + np.random.randn(len(x))
plt.plot(x, y, label = "IIR")
plt.legend()
plt.show()