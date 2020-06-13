# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:19:12 2020
https://rhodesmill.org/pyephem/quick.html#angles
@author: PC
"""

import ephem

a = ephem.degrees(3.141593)  # float: radians
print(a)

a = ephem.degrees('180:00:00')  # str: degrees
print(a)
print("180 degrees is %f radians" % a)

h = ephem.hours('1:00:00')
deg = ephem.degrees(h)
print("1h right ascension = %s degrees" % deg)

print(ephem.degrees(ephem.pi / 32))
print(ephem.degrees('5.625'))
print(ephem.degrees('5:37.5'))
print(ephem.degrees('5:37:30'))
print(ephem.degrees('5:37:30.0'))
print(ephem.hours('0.375'))
print(ephem.hours('0:22.5'))
print(ephem.hours('0:22:30'))
print(ephem.hours('0:22:30.0'))
