# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:18:22 2020
https://rhodesmill.org/pyephem/quick.html#bodies
@author: PC
"""

import ephem

line = "C/2002 Y1 (Juels-Holvorcem),e,103.7816,166.2194,128.8232,242.5695,0.0002609,0.99705756,0.0000,04/13.2508/2003,2000,g  6.5,4.0"
yh = ephem.readdb(line)
yh.compute('2007/10/1')
print('%.10f' % yh.earth_distance)
print(yh.mag)
