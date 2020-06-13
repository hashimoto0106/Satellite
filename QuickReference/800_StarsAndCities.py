# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:57:07 2020
https://rhodesmill.org/pyephem/quick.html#stars-and-cities
@author: PC
"""

import ephem

rigel = ephem.star('Rigel')
print('%s %s' % (rigel._ra, rigel._dec))

stuttgart = ephem.city('Stuttgart')
print(stuttgart.lon)
print(stuttgart.lat)
