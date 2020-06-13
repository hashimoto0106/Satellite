# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:11:32 2020
https://rhodesmill.org/pyephem/quick.html#bodies
@author: PC
"""

import ephem

gatech = ephem.Observer()
gatech.lon = '-84.39733'
gatech.lat = '33.775867'
gatech.elevation = 320
gatech.date = '1984/5/30 16:22:56'
v = ephem.Venus(gatech)

print('%s %s' % (v.alt, v.az))
