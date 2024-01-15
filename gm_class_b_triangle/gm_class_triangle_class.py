# gm_class_triangle_class.py: coded by Kinya MIURA 231126
# ---------------------------------------------------------
print('*** introducing class and function ***')
print('   *** triangle: with class ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
import numpy as np

# ========================================================
## --- class ---
class GMPoint:  # declaring class GMPoint
    def __init__(self, xx: float, yy: float) -> None:
        self.xx, self.yy = xx, yy
    def dist(self, pint):
        return np.sqrt((pint.xx-self.xx)**2 + (pint.yy-self.yy)**2)
    
class GMTriangle:  # declaring class GMTriangle
    def __init__(self, pinta: GMPoint, pintb: GMPoint, pintc: GMPoint) -> None:
        self.pinta, self.pintb, self.pintc = pinta, pintb, pintc
    def side(self):
        return self.pintb.dist(self.pintc), self.pintc.dist(self.pinta), self.pinta.dist(self.pintb)
    def area(self):
        ssa, ssb, ssc = self.side(); sss = (ssa+ssb+ssc) / 2
        return np.sqrt((sss-ssa) * (sss-ssb) * (sss-ssc) * sss)

# ========================================================
## --- main process --- ##
pinta, pintb, pintc = GMPoint(0, 0), GMPoint(4, 3), GMPoint(-3, 4)  # setting apex points
tang = GMTriangle(pinta, pintb, pintc)  # setting triangle
print(f'{(pinta.xx,pinta.yy) = }, {(pintb.xx,pintb.yy)  = }, {(pintc.xx,pintc.yy)  = }')
# (pinta.xx,pinta.yy) = (0, 0), (pintb.xx,pintb.yy)  = (4, 3), (pintc.xx,pintc.yy)  = (-3, 4)

sidea, sideb, sidec = tang.side()  # calculating sides
print(f'sidea = {sidea:g}, sideb = {sideb:g}, sidec = {sidec:g}')
# sidea = 7.07107, sideb = 5, sidec = 5

area = tang.area()  # calculating area
print(f'{area = }')
# area = 12.5