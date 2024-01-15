# gm_class_vector_e.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMVectorE: operating vector ***')
print('   *** with vector arithmetics ***')
# ---------------------------------------------------------
print('### --- section_module: (GMVectorE) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array)
def srsq(xx, yy): return sr(sq(xx)+sq(yy))
def atan2(yy, xx, deg=False):
    tht = arctan2(yy,xx)
    return r2d(tht) if deg else tht

# =========================================================
print('### --- section_class: (GMVectorE) declaring class --- ###')
class GMVectorE():
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
            f'(GMVectorE): xx = {xx:g}, yy = {yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
    ## --- section_e: functions for properties --- ##
    ## --- section_f: functions for vector analysis --- ##
    ## --- section_g: functions for vector operation --- ##
    ## --- section_h: modified operators --- ##
    def convvect(self, vect) -> ndarray:
        if isinstance(vect, GMVectorE): return vect.xxyy()
        else: return array(vect)
    def __add__(self, vect): return GMVectorE(xxyy=self.__xxyy+self.convvect(vect))
    def __radd__(self, vect): return GMVectorE(xxyy=self.convvect(vect)+self.__xxyy)
    def __sub__(self, vect): return GMVectorE(xxyy=self.__xxyy-self.convvect(vect))
    def __rsub__(self, vect): return GMVectorE(xxyy=self.convvect(vect)-self.__xxyy)
    def __mul__(self, vect): return GMVectorE(xxyy=self.__xxyy*self.convvect(vect))
    def __rmul__(self, vect): return GMVectorE(xxyy=self.convvect(vect)*self.__xxyy)
    def __truediv__(self, vect): return GMVectorE(xxyy=self.__xxyy/self.convvect(vect))
    def __rtruediv__(self, vect): return GMVectorE(xxyy=self.convvect(vect)/self.__xxyy)
    def __iadd__(self, vect): self.__xxyy += self.convvect(vect); return self
    def __isub__(self, vect): self.__xxyy -= self.convvect(vect); return self
    def __imul__(self, vect): self.__xxyy *= self.convvect(vect); return self
    def __itruediv__(self, vect): self.__xxyy /= self.convvect(vect); return self
    def __pos__(self): self.__xxyy = +self.__xxyy; return self
    def __neg__(self): self.__xxyy = -self.__xxyy; return self

# =========================================================
print('### --- section_main: (GMVectorE) main process --- ###')
## --- section_m0: calculating arithmetics ---
vecta = GMVectorE(xxyy=(4.,3.))  # creating instance
print('vecta: ', vecta)
vectb = GMVectorE(xxyy=(2.,1.))  # creating instance
print('vectb: ', vectb)
print('vecta + vectb = ', vecta + vectb)
print('vecta / vectb = ', vecta / vectb)
vecta -= vectb; print('vecta -= vectb; vecta: ', vecta)
vecta *= vectb; print('vecta *= vectb; vecta: ', vecta)

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVectorE: operating vector ***
   *** with vector arithmetics ***
### --- section_module: (GMVectorE) importing items from, module --- ###
### --- section_class: (GMVectorE) declaring class --- ###
### --- section_main: (GMVectorE) main process --- ###
vecta:  (GMVectorE): xx = 4, yy = 3, rr = 5, th(deg) = 36.8699
vectb:  (GMVectorE): xx = 2, yy = 1, rr = 2.23607, th(deg) = 26.5651
vecta + vectb =  (GMVectorE): xx = 6, yy = 4, rr = 7.2111, th(deg) = 33.6901
vecta / vectb =  (GMVectorE): xx = 2, yy = 3, rr = 3.60555, th(deg) = 56.3099
vecta -= vectb; vecta:  (GMVectorE): xx = 2, yy = 2, rr = 2.82843, th(deg) = 45
vecta *= vectb; vecta:  (GMVectorE): xx = 4, yy = 2, rr = 4.47214, th(deg) = 26.5651
'''
