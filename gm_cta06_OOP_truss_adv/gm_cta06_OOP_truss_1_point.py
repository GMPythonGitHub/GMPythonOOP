# gm_geom_1_point.py: coded by Kinya MIURA 230518
# ---------------------------------------------------------
print("*** (GMPoint) class for point ***")
print("   *** class GMVector is inherited ***")
# ---------------------------------------------------------
print("### --- section_module: (GMPoint) importing items from module --- ###")
from numpy import (
    deg2rad as d2r, rad2deg as r2d, cos, sin, tan, arccos, arctan2,
    ndarray, array, inner, outer, cross )
from numpy.linalg import norm
import copy
from gm_cta06_OOP_truss_0_vector import GMVector

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
print("### --- section_a: (GMPoint) declaring class --- ###")
class GMPoint(GMVector):  # inheriting class GMVector
    ## --- section_b: (GMPoint) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (0., 0.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True):
        super().__init__(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg )
    ## --- section_c: (GMPoint) setting functions --- ##
    def set_point(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True) -> None:
        self.set_vector(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
    ## --- section_d: (GMPoint) string function for print() --- ##
    def __str__(self) -> str:
        return '(GMVector) ' + super().__str__()
    def printclass(self, idx: str = '') -> None:
        print(
            idx + ':: GMPoint ::\n  '
            + self.__str__() )
    ## --- section_e: (GMPoint) functions for analyzing points --- ##
    def copy(self) -> object:
        return copy.deepcopy(self)
    def vect2pint(self, pint: object, cnv: bool = True) -> ndarray:
        return pint.xxyy(cnv) - self.xxyy(cnv)
    def dist2pint(self, pint: object, cnv: bool = True) -> float:
        return norm(self.vect2pint(pint, cnv=cnv))
    def dirc2pint(self, pint: object, deg: bool = True) -> float:
        v2p = self.vect2pint(pint)
        return gmatan2(v2p[1], v2p[0], deg=deg)
    def unitvect2pint(self, pint: object) -> ndarray:
        vect2pint = self.vect2pint(pint)
        return vect2pint / norm(vect2pint)

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMPoint) main process --- ###")
    ## --- section_ma: (GMPoint) creating class instances --- ##
    pinta = GMPoint(xxyy=(1., 2.), unit=1.); pinta.printclass('pinta -> ')
    pintb = GMPoint(xxyy=(2., 1.), unit=1.); pintb.printclass('pintb -> ')
    ## --- section_mb: (GMPoint) calculating unit distance and unit vector --- ##
    print(f'{pinta.unitvect() = }')  # GMVector
    print(f'{pinta.vect2pint(pintb) = }')
    print(f'{pinta.dist2pint(pintb) = }')
    print(f'{pinta.unitvect2pint(pintb) = }')
    print(f'{pintb.unitvect() = }')  # GMVector
    print(f'{pintb.vect2pint(pinta) = }')
    print(f'{pintb.dist2pint(pinta) = }')
    print(f'{pintb.unitvect2pint(pinta) = }')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMPoint) class for point ***
      *** class GMVector is inherited ***
    ### --- section_module: (GMPoint) importing items from module --- ###
    
    *** (GMVector) class for vector ***
    ### --- section_module: (GMVector) importing items from module --- ###
    ### --- section_class: (GMVector) declaring class --- ###
    ### --- section_a: (GMPoint) declaring class --- ###
    ### --- section_m: (GMPoint) main calculation process --- ###
    pinta -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unit = 1
    pintb -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unit = 1
    pinta.unitvect() = array([0.4472136 , 0.89442719])
    pinta.vect2pint(pintb) = array([ 1., -1.])
    pinta.dist2pint(pintb) = 1.4142135623730951
    pinta.unitvect2pint(pintb) = array([ 0.70710678, -0.70710678])
    pintb.unitvect() = array([0.89442719, 0.4472136 ])
    pintb.vect2pint(pinta) = array([-10.,  10.])
    pintb.dist2pint(pinta) = 1.4142135623730951
    pintb.unitvect2pint(pinta) = array([-0.70710678,  0.70710678])
    '''
