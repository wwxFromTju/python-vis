#!/usr/bin/env python
# encoding=utf-8

import pygal.maps.world as hehe

wm = hehe.World()
wm.title = 'just world'
wm.add('North', {'ca': 34126000, 'us':309349000, 'mx': 113423000})

wm.render_to_file('na_population.svg')