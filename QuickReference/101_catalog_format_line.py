# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:18:22 2020
https://rhodesmill.org/pyephem/quick.html#bodies
@author: PC
"""

import ephem

line1 = "ISS (ZARYA)"
line2 = "1 25544U 98067A   03097.78853147  .00021906  00000-0  28403-3 0  8652"
line3 = "2 25544  51.6361  13.7980 0004256  35.6671  59.2566 15.58778559250029"

iss = ephem.readtle(line1, line2, line3)
iss.compute('2003/3/23')

print('%s %s' % (iss.sublong, iss.sublat))
