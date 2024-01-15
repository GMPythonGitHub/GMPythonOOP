# gm_coord_point_2d_class.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and class ***')
print('   *** coordinate point movement in 2d with class ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (cos, sin, rad2deg as r2d, deg2rad as d2r)

# =========================================================
## --- class --- ##
class GMTrans:
    def __init__(self, xx, yy) -> None:
        self.xx, self.yy = None, None
        # initializing xx, yy: instance variables
        self.set_xxyy(xx, yy)
    def set_xxyy(self, xx, yy) -> None:  # setting point
        self.xx, self.yy = xx, yy
        self.xxyy()
    def xxyy(self) -> tuple:  # getting point
        print(f'xx = {self.xx:g}, yy = {self.yy:g}')
        return self.xx, self.yy
    def shift(self, ssx, ssy) -> tuple:  # shifting point
        self.xx += ssx; self.yy += ssy
        print(f'ssx = {ssx:g}, ssy = {ssy:g} >> ', end='')
        return self.xxyy()
    def scale(self, ccx, ccy) -> tuple:  # scaling point
        self.xx *= ccx; self.yy *= ccy
        print(f'ccx = {ccx:g}, ccy = {ccy:g} >> ', end='')
        return self.xxyy()
    def revolve(self, ps) -> tuple:  # revolving point
        self.xx, self.yy = (
            + self.xx * cos(ps) - self.yy * sin(ps),
            + self.xx * sin(ps) + self.yy * cos(ps) )
        print(f'ps = {r2d(ps):g} >> ', end='')
        return self.xxyy()

# =========================================================
## --- main process --- ##
xx, yy = 3, 4
trans = GMTrans(xx = 0, yy = 0)  # creating instance of GMTrans
# xx = 3, yy = 4
trans.shift(ssx=2, ssy=1)  # shifting point
# ssx = 2, ssy = 1 >> xx = 5, yy = 5
trans.scale(ccx=2, ccy=3)  # scaling point
# ccx = 2, ccy = 3 >> xx = 10, yy = 15
trans.revolve(ps=d2r(90))  # revolving point
# ps = 90 >> xx = -15, yy = 10
