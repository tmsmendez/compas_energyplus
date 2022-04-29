import os
import compas_energyplus
from compas_energyplus.datastructures import Window

for i in range(50): print('')

w = 10
l = 12
h = 3

w_ = w * .3
h_ = h * .3

v0 = [w_, 0, h_]
v1 = [w_ *  2, 0, h_]
v2 = [w_ * 2, 0, h_ * 2]
v3 = [0, 0, h_ * 2]

win = Window()
win.name = 'w1'
win.nodes = [v0, v1, v2, v3]
win.building_surface = 'zone1_0'
win.construction = 'window_construction'
win.to_json(os.path.join(compas_energyplus.DATA, 'building_parts', 'w1.json'))
