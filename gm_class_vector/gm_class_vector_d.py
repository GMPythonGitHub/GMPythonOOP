# gm_class_vector_d.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMVectorD: operating vector ***')
print('   *** with vector calculation ***')
# ---------------------------------------------------------
print('### --- section_module: (GMVectorD) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array)
def srsq(xx, yy): return sr(sq(xx)+sq(yy))
def atan2(yy, xx, deg=False):
    tht = arctan2(yy,xx)
    return r2d(tht) if deg else tht

aa, bb = array([1,2,3]), array([3])
print (aa, bb)
print(array(aa), array(bb))
print(aa * array(bb))
print(aa + array(bb))

# =========================================================
print('### --- section_class: (GMVectorD) declaring class --- ###')
class GMVectorD():
    ## --- section_a: initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = None, rrth: tuple = None, deg: bool = True) -> None:
        self.__xxyy = None
        self.set_vect(xxyy=xxyy, rrth=rrth, deg=deg)
    ## --- section_b: setting functions --- ##
    def set_vect(self,
            xxyy: tuple = None, rrth: tuple = None, deg: bool = True) -> None:
        if xxyy is not None: self.__xxyy = array(xxyy)
        if rrth is not None:
            rr, th = rrth
            if deg: th = d2r(th)
            self.__xxyy = array([rr * cos(th), rr * sin(th)])
    ## --- section_c: getting functions --- ##
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, deg: bool = False) -> ndarray:
        xx, yy = self.__xxyy
        return array([srsq(xx,yy), atan2(yy,xx,deg=deg)])
    ## --- section_d: string function for print() --- ##
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(True)
        return (
            f'(GMVectorD): xx = {xx:g}, yy = {yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
    ## --- section_e: functions for properties --- ##
    ## --- section_f: functions for vector analysis --- ##
    ## --- section_g: functions for vector operation --- ##
    def convvect(self, vect) -> object:
        if isinstance(vect, (int, float, complex)): return vect
        elif isinstance(vect, (tuple, list, ndarray)): return array(vect)
        elif isinstance(vect, GMVectorD): return vect.xxyy()
        else: return None
    def add(self, vect: object) -> None: self.__xxyy += self.convvect(vect)
    def sub(self, vect: object) -> None: self.__xxyy -= self.convvect(vect)
    def mul(self, vect: object) -> None: self.__xxyy *= self.convvect(vect)
    def div(self, vect: object) -> None: self.__xxyy /= self.convvect(vect)

# =========================================================
print('### --- section_main: (GMVectorD) main process --- ###')
## --- section_m0: calculating arithmetics --- ##
vect = GMVectorD(xxyy=(4.,3.))  # creating instance
print('vect = ', vect)
vecta = GMVectorD(xxyy=(2.,1.))  # creating instance
print('vecta = ', vecta)
vect.add(2); print('vect += 2: ', vect)
vect.sub((1,2)); print('vect -= (1,2): ', vect)
vect.mul(vecta); print('vect *= vecta: ', vect)
vect.div(2.); print('vect /= 2.: ', vect)

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVectorD: operating vector ***
   *** with vector calculation ***
### --- section_module: (GMVectorD) importing items from module --- ###
### --- section_class: (GMVectorD) declaring class --- ###
### --- section_main: (GMVectorD) main process --- ###
vect =  (GMVectorD): xx = 4, yy = 3, rr = 5, th(deg) = 36.8699
vecta =  (GMVectorD): xx = 2, yy = 1, rr = 2.23607, th(deg) = 26.5651
vect += 2:  (GMVectorD): xx = 6, yy = 5, rr = 7.81025, th(deg) = 39.8056
vect -= (1,2):  (GMVectorD): xx = 5, yy = 3, rr = 5.83095, th(deg) = 30.9638
vect *= vecta:  (GMVectorD): xx = 10, yy = 3, rr = 10.4403, th(deg) = 16.6992
vect /= 2.:  (GMVectorD): xx = 5, yy = 1.5, rr = 5.22015, th(deg) = 16.6992
'''
