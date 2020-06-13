# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:54:01 2020
https://rhodesmill.org/pyephem/quick.html#coordinate-conversion
https://rhodesmill.org/pyephem/coordinates
@author: PC
"""

import ephem


m = ephem.Mars('1990/12/13')
print('%s %s' % (m.a_ra, m.a_dec))

ecl = ephem.Ecliptic(m)
print('%s %s' % (ecl.lon, ecl.lat))

gal = ephem.Galactic(m)
print('%s %s' % (gal.lon, gal.lat))

print(ecl.epoch)
