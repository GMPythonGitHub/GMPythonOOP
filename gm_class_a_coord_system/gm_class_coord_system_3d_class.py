# gm_class_coord_system_2d_class.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point in 3d with class ***')
print('   *** rectangular (xx-yy) <> circular (rr-th) ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# ========================================================
## --- class --- ##
class CoodPoint:
    def __init__(self, xx, yy, zz) -> None:
        self.xx, self.yy, self.zz = None, None, None  # initializing xx-yy-zz
        self.set_xxyyzz(xx, yy, zz)
    def set_xxyyzz(self, xx, yy, zz) -> None:  # setting xx-yy-zz
        self.xx, self.yy, self.zz = xx, yy, zz
    def set_rrthph(self, rr, th, ph) -> None:  # setting rr-th-ph
        self.xx, self.yy, self.zz = (  # from rr-th-ph to xx-yy-zz
            rr * sin(ph) * cos(th), rr * sin(ph) * sin(th), rr * cos(ph) )
    def xxyyzz(self) -> tuple:  # getting xx-yy-zz
        return self.xx, self.yy, self.zz  # instance variables
    def rrthph(self) -> tuple:  # getting rr-th-ph
        return (  # from xx-yy-zz to rr-th-ph
            sqrt(self.xx**2+self.yy**2+self.zz**2), atan2(self.yy, self.xx),
            atan2(sqrt(self.xx**2+self.yy**2), self.zz) )

# ========================================================
## --- main process ---
xx, yy, zz = 3, 4, 5
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5
point = CoodPoint(xx, yy, zz)  # creating instance of class CoordPoint
rr, th, ph = point.rrthph()
print(f'rr = {rr:g}, th = {r2d(th):g}, ph = {r2d(ph):g}')
# rr = 7.07107, th = 53.1301, ph = 45
point.set_rrthph(rr, th, ph)  # setting rr-th-ph
xx, yy, zz = point.xxyyzz()
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5