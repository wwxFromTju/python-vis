#!/usr/bin/env python
# encoding=utf-8

import json

import pygal.maps.world as hehe

from country_code import get_country_code

filename = 'data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

wm = hehe.World()
wm.title = 'just world map'
wm.add('2010', cc_populations)

wm.render_to_file('world_populations_map.svg')

