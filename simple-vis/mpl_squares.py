#!/usr/bin/env python
# encoding=utf-8

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]


plt.plot(input_values, squares, linewidth=5)

plt.title('just title', fontsize=24)
plt.xlabel('x axis', fontsize=24)
plt.ylabel('y axis', fontsize=24)

plt.tick_params(axis='both', labelsize=24)

plt.show()