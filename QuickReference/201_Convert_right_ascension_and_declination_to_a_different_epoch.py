# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:45:01 2020
https://rhodesmill.org/pyephem/coordinates
@author: PC
"""

import ephem


m = ephem.Mars('2003/08/27', epoch=ephem.J2000)
print('%s %s' % (m.a_ra, m.a_dec))

p = ephem.Equatorial(m, epoch=ephem.B1950)
print('%s %s' % (p.ra, p.dec))

north_pole = ephem.Equatorial('0', '90', epoch=ephem.J2000)
ancient_pole = ephem.Equatorial(north_pole, epoch='-2500')
print('%s %s' % (ancient_pole.ra, ancient_pole.dec))
