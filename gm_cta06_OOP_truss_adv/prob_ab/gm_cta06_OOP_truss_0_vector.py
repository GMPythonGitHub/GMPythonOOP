## gm_cta06_OOP_truss_0_vector.py: coded by Kinya MIURA 230523
# ---------------------------------------------------------
print("*** (GMVector) class for vector ***")
# ---------------------------------------------------------
print("### --- section_module: (GMVector) importing items from module --- ###")
from numpy import (
    deg2rad as d2r, rad2deg as r2d, cos, sin, tan, arccos, arctan2,
    ndarray, array, inner, outer, cross )
from numpy.linalg import norm
import copy
def gmcos(th: float, deg: bool = False) -> float:
    return cos(d2r(th)) if deg else cos(th)
def gmsin(th: float, deg: bool = False) -> float:
    return sin(d2r(th)) if deg else sin(th)
def gmtan(th: float, deg: bool = False) -> float:
    return tan(d2r(th)) if deg else tan(th)
def gmacos(xx: float, deg=False) -> float:
    return r2d(arccos(xx)) if deg else arccos(xx)
def gmatan2(yy: float, xx: float, deg=False) -> float:
    return r2d(arctan2(yy, xx)) if deg else arctan2(yy, xx)

# =========================================================
print("### --- section_class: (GMVector) declaring class --- ###")
class GMVector():
    ## --- section_a: (GMVector) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (0., 0.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True ):
        self.__xxyy, self.__unit = None, None
        self.set_vector(xxyy, rrth, unit=unit, cnv=cnv, deg=deg)
    ## --- section_b: (GMVector) setting functions --- ##
    def set_vector(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True ) -> None:
        if unit is not None: self.__unit = unit
        if rrth is not None:
            self.set_rrth(rrth, cnv=cnv, deg=deg)
        elif xxyy is not None:
            self.set_xxyy(xxyy, cnv=cnv)
    def set_xxyy(self, xxyy: tuple, cnv: bool = True) -> None:
        self.__xxyy = array(xxyy) * self.__unit if cnv else array(xxyy)
    def set_rrth(self, rrth: tuple, cnv: bool = True, deg: bool = True) -> None:
        rr, th = rrth
        if cnv: rr *= self.__unit
        self.__xxyy = rr * array(
            (gmcos(th,deg=deg), gmsin(th,deg=deg)) )
    ## --- section_c: (GMVector) getting functions --- ##
    def unit(self) -> float:
        return self.__unit
    def xxyy(self, cnv: bool = True) -> ndarray:
        if cnv: return self.__xxyy / self.__unit
        else: return self.__xxyy
    def rrth(self, cnv: bool = True, deg: bool = True) -> ndarray:
        rr = norm(self.__xxyy) / self.__unit if cnv else norm(self.__xxyy)
        th = gmatan2(self.__xxyy[1], self.__xxyy[0], deg=deg)
        return array((rr, th))
    ## --- section_d: (GMVector) string function for print() --- ##
    def __str__(self) -> str:
        xxyy = self.xxyy(); rrth = self.rrth()
        return (
            f'xxyy = {xxyy} : rrth = {rrth} : unit = {self.__unit:g}' )
    def printclass(self, idx: str = '') -> None:
        print(
            idx + ':: GMVector ::\n  '
            + self.__str__() )
    ## --- section_e: (GMVector) functions for properties --- ##
    def copy(self) -> object:
        return copy.deepcopy(self)
    def leng(self, cnv: bool = True) -> float:
        val = norm(self.__xxyy)
        return val / self.__unit if cnv else val
    def dirc(self, deg: bool = True) -> float:
        return gmatan2(self.__xxyy[1], self.__xxyy[0], deg=deg)
    def unitvect(self) -> tuple:
        return self.__xxyy / norm(self.__xxyy)
    ## --- section_f: (GMVector) functions for analyzing vectors --- ##
    def inner2vect(self, vect: object, cnv: bool = True) -> ndarray:  # inner product
        return inner(self.xxyy(cnv), vect.xxyy())
    def outer2vect(self, vect: object, cnv: bool = True) -> ndarray:  # outer product
        return outer(self.xxyy(cnv), vect.xxyy(cnv))
    def cross2vect(self, vect: object, cnv: bool = True) -> ndarray:  # cross product
        return cross(self.xxyy(cnv), vect.xxyy(cnv))
    ## --- section_g: (GMVector) functions for operating vectors --- ##
    def convvect(self, vect) -> object:
        if isinstance(vect, GMVector): return vect.xxyy(False)
        else: return array(vect)
    def add(self, vect: object) -> None: self.__xxyy += self.convvect(vect)
    def sub(self, vect: object) -> None: self.__xxyy -= self.convvect(vect)
    def mul(self, vect: object) -> None: self.__xxyy *= self.convvect(vect)
    def div(self, vect: object) -> None: self.__xxyy /= self.convvect(vect)

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMVector) main process --- ###")
    ## --- section_ma: (GMVector) creating class instances --- ##
    vecta = GMVector(xxyy=(1., 1.), unit=1.); vecta.printclass('vecta -> ')
    vectb = GMVector(xxyy=(1., -1.), unit=1.); vectb.printclass('vectb -> ')
    ## --- section_mb: (GMVector) calculating vector properties --- ##
    print(f'{vecta.leng() = }')
    print(f'{vecta.dirc() = }')
    print(f'{vecta.unitvect() = }')
    print(f'{vectb.leng() = }')
    print(f'{vectb.dirc() = }')
    print(f'{vectb.unitvect() = }')
    ## --- section_mc: (GMVector) calculating vector products --- ##
    print(f'{vecta.inner2vect(vectb) = }')
    print(f'{vecta.outer2vect(vectb) = }')
    print(f'{vecta.cross2vect(vectb) = }')
    print(f'{vectb.inner2vect(vecta) = }')
    print(f'{vectb.outer2vect(vecta) = }')
    print(f'{vectb.cross2vect(vecta) = }')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMVector) class for vector ***
    ### --- section_module: (GMVector) importing items from module --- ###
    ### --- section_class: (GMVector) declaring class --- ###
    ### --- section_main: (GMVector) main process --- ###
    vecta -> :: GMVector ::
      xxyy = [1. 1.] : rrth = [ 1.41421356 45.        ] : unit = 1
    vectb -> :: GMVector ::
      xxyy = [ 1. -1.] : rrth = [  1.41421356 -45.        ] : unit = 1
    vecta.leng() = 1.4142135623730951
    vecta.dirc() = 45.0
    vecta.unitvect() = array([0.70710678, 0.70710678])
    vectb.leng() = 1.4142135623730951
    vectb.dirc() = -45.0
    vectb.unitvect() = array([ 0.70710678, -0.70710678])
    vecta.inner2vect(vectb) = 0.0
    vecta.outer2vect(vectb) = array([[ 1., -1.], [ 1., -1.]])
    vecta.cross2vect(vectb) = array(-2.)
    vectb.inner2vect(vecta) = 0.0
    vectb.outer2vect(vecta) = array([[ 1.,  1.], [-1., -1.]])
    vectb.cross2vect(vecta) = array(2.)
    '''
