#!/usr/bin/env python
# encoding=utf-8

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# plt.scatter(x_values, y_values, s=40, edgecolors='none', c='red')
# plt.scatter(x_values, y_values, s=40, edgecolors='none', c=(0, 0, 0.8))
plt.scatter(x_values, y_values, s=40, edgecolors='none', c=y_values, cmap=plt.cm.Blues)

plt.title('just title', fontsize=24)
plt.xlabel('x axis', fontsize=24)
plt.ylabel('y axis', fontsize=24)

plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('scatter.png', bbox_inches='tight')
plt.show()
