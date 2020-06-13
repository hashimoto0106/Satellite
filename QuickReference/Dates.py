# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:59:11 2020
https://rhodesmill.org/pyephem/quick.html#dates
@author: PC
"""

import ephem

d = ephem.Date('1997/3/9 5:13')
print(d)
print(d.triple())
print(d.tuple())
print(d + ephem.hour)
print(ephem.date(d + ephem.hour))
print(ephem.date(d + 1))

ephem.Date(35497.7197916667)
ephem.Date('1997/3/10.2197916667')
ephem.Date('1997/3/10 05.275')
ephem.Date('1997/3/10 05:16.5')
ephem.Date('1997/3/10 05:16:30')
ephem.Date('1997/3/10 05:16:30.0')
ephem.Date((1997, 3, 10.2197916667))
ephem.Date((1997, 3, 10, 5, 16, 30.0))

d = ephem.Date('1997/3/9 5:13')
ephem.localtime(d)
print(ephem.localtime(d))

d = ephem.Date('1997/3/9 5:13')
ephem.to_timezone(d, ephem.UTC)
print(ephem.to_timezone(d, ephem.UTC))
