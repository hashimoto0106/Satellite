# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:02:04 2020
https://rhodesmill.org/pyephem/quick.html#equinoxes-solstices
@author: PC
"""

import ephem

d1 = ephem.next_equinox('2000')
print(d1)
d2 = ephem.next_solstice(d1)
print(d2)
t = d2 - d1
print("Spring lasted %.1f days" % t)

print(ephem.previous_solstice('2000'))
print(ephem.next_solstice('2000'))

print(ephem.previous_equinox('2000'))
print(ephem.next_equinox('2000'))

print(ephem.previous_vernal_equinox('2000'))
print(ephem.next_vernal_equinox('2000'))
