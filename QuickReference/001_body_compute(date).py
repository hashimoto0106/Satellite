# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:02:38 2020
https://rhodesmill.org/pyephem/quick.html#bodies
@author: PC
"""

import ephem


j = ephem.Jupiter()
j.compute('1986/2/8')
print('%s %s' % (j.ra, j.dec))

j.compute('1986/2/8', epoch='2000')
print('%s %s' % (j.ra, j.dec))

j.compute('1986/2/8', epoch='2000')
print('%s %s' % (j.a_ra, j.a_dec))

j.compute('1986/2/8', epoch='1950')
print('%s %s' % (j.a_ra, j.a_dec))
