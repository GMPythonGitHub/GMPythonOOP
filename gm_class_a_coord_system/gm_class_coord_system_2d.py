# gm_class_coord_system_2d.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point in 2d ***')
print('   *** rectangular (xx-yy) <> circular (rr-th) ***')
# --------------------------------------------------------
## --- importing items from module --- ##
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# ========================================================
## --- main process --- ##
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')
# xx = 3, yy = 4

rr, th = sqrt(xx**2+yy**2), atan2(yy, xx)  # from xx-yy to rr-th
print(f'rr = {rr:g}, th = {r2d(th):g}')
# rr = 5, th = 53.1301

xx, yy = rr * cos(th), rr * sin(th)  # from rr-th to xx-yy
print(f'xx = {xx:g}, yy = {yy:g}')
# xx = 3, yy = 4
