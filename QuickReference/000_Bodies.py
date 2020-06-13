# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:37:18 2020
https://rhodesmill.org/pyephem/quick.html#bodies
@author: PC
"""

import ephem


m = ephem.Mars()
print(m.name)

a = ephem.star('Arcturus')
print(a.name)

m = ephem.Mars('2003/8/27')
print('%s %s %.10f' % (m.name, m.elong, m.size))
