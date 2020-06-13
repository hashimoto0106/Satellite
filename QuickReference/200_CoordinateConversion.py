# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:31:00 2020
https://rhodesmill.org/pyephem/quick.html#coordinate-conversion
https://rhodesmill.org/pyephem/coordinates
@author: PC
"""

import ephem


np = Equatorial('0', '90', epoch='2000')  # 赤道
g = Galactic(np)  # 銀河
print('%s %s' % (g.lon, g.lat))
