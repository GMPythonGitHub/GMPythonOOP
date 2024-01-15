# gm_class_coord_system_3d_func.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point in 3d with function ***')
print('   *** rectangular (xx-yy-zz) <> circular (rr-th-ph) ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# ========================================================
## --- function ---
def xxyyzz2rrthph(xx, yy, zz):  # from xx-yy-zz to rr-th-ph
    rr, th, ph = (
        sqrt(xx ** 2 + yy ** 2 + zz ** 2), atan2(yy, xx), atan2(sqrt(xx ** 2 + yy ** 2), zz))
    return rr, th, ph
def rrthph2xxyyzz(rr, th, ph):  # from rr-th-ph to xx-yy-zz
    xx, yy, zz = (
        rr * sin(ph) * cos(th), rr * sin(ph) * sin(th), rr * cos(ph))
    return xx, yy, zz

# ========================================================
## --- main process ---
xx, yy, zz = 3, 4, 5
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5
rr, th, ph = xxyyzz2rrthph(xx, yy, zz)  # from xx-yy-zz to rr-th-ph
print(f'rr = {rr:g}, th = {r2d(th):g}, ph = {r2d(ph):g}')
# rr = 7.07107, th = 53.1301, ph = 45
xx, yy, zz = rrthph2xxyyzz(rr, th, ph)  # from rr-th-ph to xx-yy-zz
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5