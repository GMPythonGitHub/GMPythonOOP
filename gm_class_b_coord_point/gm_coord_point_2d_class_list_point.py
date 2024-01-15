# gm_coord_point_2d_class_list_point.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and class ***')
print('   *** coordinate point movement in 2d with class ***')
print('   *** generating a list of points ***')

# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (cos, sin, rad2deg as r2d, deg2rad as d2r)

# =========================================================
## --- class --- ##
class GMTrans:
    def __init__(self, xx = 0, yy = 0) -> None:
        self.xx, self.yy = None, None
        # initializing xx, yy: instance variables
        self.set_xxyy(xx, yy)
    def set_xxyy(self, xx, yy) -> tuple:  # setting point
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
xxyyo = [(0,0), (1,0), (1,1), (0,1), (0,0)]  # generating a list of points
trans = GMTrans()  # creating instance of GMTrans
xxyym = []
for xxyy in xxyyo:
    trans.set_xxyy(*xxyy)
    xxyym.append(list(trans.revolve(ps=d2r(45))))  # shifting point
print(xxyyo, xxyym)
## --- drawing figure --- ##
from matplotlib import pyplot as plt
xxo = [xxyy[0] for xxyy in xxyyo]
yyo = [xxyy[1] for xxyy in xxyyo]
plt.plot(xxo, yyo)
xxm = [xxyy[0] for xxyy in xxyym]
yym = [xxyy[1] for xxyy in xxyym]
plt.plot(xxm,yym)
plt.savefig('gm_coord_point_2d_class_list_point.png')
plt.show()


