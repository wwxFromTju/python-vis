#!/usr/bin/env python
# encoding=utf-8

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'github python'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description httpie'},
    {'value': 15028, 'label': 'Description django'},
    {'value': 14798, 'label': 'Description flask'}
]

chart.add('',plot_dicts)
chart.render_to_file('bar_des.svg')
