# gm_class_coord_system_2d_class.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point in 2d with class ***')
print('   *** rectangular (xx-yy) <> circular (rr-th) ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# ========================================================
## --- class --- ##
class CoodPoint:
    def __init__(self, xxx, yy) -> None:
        self.xx, self.yy = None, None  # initializing xx-yy
        self.set_xxyy(xx, yy)
    def set_xxyy(self, xx, yy) -> None:  # setting xx-yy
        self.xx, self.yy = xx, yy
    def set_rrth(self, rr, th) -> None:  # setting rr-th to xx-yy
        self.xx, self.yy = rr * cos(th), rr * sin(th)
    def xxyy(self) -> tuple:  # getting rec
        return self.xx, self.yy  # instance variables
    def rrth(self) -> tuple:
        return sqrt(self.xx**2+self.yy**2), atan2(self.yy, self.xx)

# ========================================================
## --- main process --- ##
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')
# xx = 3, yy = 4
point = CoodPoint(xx, yy)  # creating instance of class CoordPoint
rr, th = point.rrth()
print(f'rr = {rr:g}, th = {r2d(th):g}')
# rr = 5, th = 53.1301
point.set_rrth(rr, th)  # setting rr-th
xx, yy = point.xxyy()
print(f'xx = {xx:g}, yy = {yy:g}')
# xx = 3, yy = 4
