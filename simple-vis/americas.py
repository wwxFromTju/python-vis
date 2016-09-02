#!/usr/bin/env python
# encoding=utf-8

import pygal.maps.world as hehe

wm = hehe.World()
wm.title = "just world"

wm.add('North American', ['ca', 'mx', 'us'])
wm.add('Central American', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South American', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('american.svg')