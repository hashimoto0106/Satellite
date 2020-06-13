# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:56:40 2020
https://rhodesmill.org/pyephem/quick.html#coordinate-conversion
https://rhodesmill.org/pyephem/coordinates
@author: PC
"""

import ephem


m = ephem.Mars('1980/2/25')
ma = ephem.Equatorial(m.ra, m.dec, epoch='1980/2/25')
me = ephem.Ecliptic(ma)
print('%s %s' % (me.lon, me.lat))
