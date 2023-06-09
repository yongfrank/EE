'''
Author: Frank Chu
Date: 2023-02-22 10:03:38
LastEditors: Frank Chu
LastEditTime: 2023-02-22 10:10:46
FilePath: /EE/DSP/sampling.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import numpy as np
from matplotlib import pyplot as plt
N = 20
fs = 500
n = np.linspace(0, N - 1, N)
x_t = np.sin(200 * np.pi * 1 / fs * n)

plt.stem(n, x_t)
plt.legend()
plt.show()