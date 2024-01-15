# gm_class_coord_system_3d.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point in 3d ***')
print('   *** rectangular (xx-yy-zz) <> circular (rr-th-ph) ***')
# ---------------------------------------------------------
## --- importing items from module ---
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# ========================================================
## --- main process ---
xx, yy, zz = 3, 4, 5
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5

rr, th, ph = (  # from xx-yy-zz to tt-th-ph
    sqrt(xx**2+yy**2+zz**2), atan2(yy, xx), atan2(sqrt(xx**2+yy**2), zz) )
print(f'rr = {rr:g}, th = {r2d(th):g}, ph = {r2d(ph):g}')
# rr = 7.07107, th = 53.1301, ph = 45

xx, yy, zz = (  # from rr-th-ph to xx-yy-zz
    rr * sin(ph) * cos(th), rr * sin(ph) * sin(th), rr * cos(ph) )
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5