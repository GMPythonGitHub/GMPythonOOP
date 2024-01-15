# gm_class_vector_b.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMVectorB: operating vector ***')
print('   *** with circular coordinate system ***')
# ---------------------------------------------------------
print('### --- section_module: (GMVectorB) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
def srsq(xx, yy) -> float: return sr(sq(xx)+sq(yy))
def atan2(yy, xx, deg=False) -> float:
    tht = arctan2(yy,xx)
    return r2d(tht) if deg else tht

# =========================================================
print('### --- section_class: (GMVectorB) declaring class --- ###')
class GMVectorB():
    ## --- section_a: initializing class instance --- ##
    def __init__(self,
            xx: float = None, yy: float = None,
            rr: float = None, th: float = None, deg: bool = True) -> None:
        self.__xx, self.__yy = None, None  # instance variables
        self.set_vect(xx=xx, yy=yy, rr=rr, th=th, deg=deg)
    ## --- section_b: setting functions --- ##
    def set_vect(self,
            xx: float = None, yy: float = None,
            rr: float = None, th: float = None, deg: bool = True) -> None:
        if xx is not None: self.__xx = xx
        if yy is not None: self.__yy = yy
        if rr is not None or th is not None:
            if rr is None: rr = srsq(self.__xx,self.__yy)
            if th is None: th = atan2(self.__yy,self.__xx,deg=deg)
            else: th = d2r(th) if deg else th
            self.__xx, self.__yy = rr * cos(th), rr * sin(th)
    ## --- section_c: getting functions --- ##
    def xxyy(self) -> tuple:
        return self.__xx, self.__yy
    def rrth(self, deg: bool = False) -> tuple:
        return srsq(self.__xx,self.__yy), atan2(self.__xx,self.__yy,deg=deg)
    ## --- section_d: string function for print() --- ##
    def __str__(self) -> str:
        rr, th = self.rrth(True)
        return (
            f'(GMVectorB): xx = {self.__xx:g}, yy = {self.__yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
    ## --- section_e: functions for properties --- ##
    def leng(self) -> float:
        return self.rrth()[0]  # rr
    def dirc(self, deg: bool = False) -> float:
        return self.rrth(deg=deg)[1]  # th
    def unitvect(self) -> tuple:
        leng = self.leng()
        return self.__xx / leng, self.__yy / leng

# =========================================================
print('### --- section_main: (GMVectorB) main process --- ###')
## --- section_m0: calculating arithmetics --- ##
vect = GMVectorB(4., 3.)  # creating instance
print(vect, f'\n{vect.unitvect() = }')
vect.set_vect(xx=5., yy=5.)  # setting instance valuables
print(vect, f'\n{vect.unitvect() = }')
vect.set_vect(rr=4., th=30., deg=True)  # setting instance valuables
print(vect, f'\n{vect.unitvect() = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVectorB: operating vector ***
   *** with circular coordinate system ***
### --- section_module: (GMVectorB) importing items from, module --- ###
### --- section_class: (GMVectorB) declaring class --- ###
### --- section_main: (GMVectorB) main process --- ###
(GMVectorB): xx = 4, yy = 3, rr = 5, th(deg) = 53.1301 
vect.unitvect() = (0.8, 0.6)
(GMVectorB): xx = 5, yy = 5, rr = 7.07107, th(deg) = 45 
vect.unitvect() = (0.7071067811865475, 0.7071067811865475)
(GMVectorB): xx = 3.4641, yy = 2, rr = 4, th(deg) = 60 
vect.unitvect() = (0.8660254037844387, 0.49999999999999994)
'''
