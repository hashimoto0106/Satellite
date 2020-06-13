# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:29:06 2020
TLE:https://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
@author: PC
"""

import ephem
import datetime
from math import degrees as deg

# Observer(観測者)クラスのインスタンスを作成。
shinjuku = ephem.Observer()
shinjuku.lat = '35.6846'
shinjuku.lon = '139.7106'
shinjuku.elevation = 60
shinjuku.date = datetime.datetime.utcnow() # 任意の年月日の位置を求められる

line1 = 'ISS'
line2 = '1 25544U 98067A   20048.52024880  .00016717  00000-0  10270-3 0  9000'
line3 = '2 25544  51.6378 225.5202 0004926 282.0303  78.0295 15.49172297 13304'
iss = ephem.readtle(line1, line2, line3)

# shinjukuから見た位置
iss.compute(shinjuku)
print(deg(iss.alt)) # -51.61249863302519
print(deg(iss.az)) # 142.92199525046195

# ISSがいる位置
iss.compute(datetime.datetime.utcnow())
print(deg(iss.sublat)) # -50.990213758123666
print(deg(iss.sublong)) # -139.8713732199458
print(iss.elevation) # 433325.5
print(iss.eclipsed) # True
