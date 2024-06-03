# gm_cta06_OOP_truss_adv1_member.py: coded by Kinya MIURA 230518
# ---------------------------------------------------------
print("*** (GMTrussMember) class for truss member ***")
print("  *** class GMTrussNode is embedded as nodea and nodeb ***")
# ---------------------------------------------------------
print("### --- section_module: (GMTrussMember) importing items from module --- ##")
from numpy import (ndarray, append, inner, outer)
import copy
from gm_cta06_OOP_truss_adv0_node import (GMTrussNode)

# =========================================================
print("### --- section_class: (GMTrussMember) declaring class --- ###")
class GMTrussMember():
    ## --- section_a: (GMTrussMember) initializing class instance --- ##
    def __init__(self,
            nodea: GMTrussNode, nodeb: GMTrussNode,
            area: float = 10., yong: float = 205., cnv: bool = True ):
        self._nodea, self._nodeb = nodea, nodeb
        # node A and node B
        self.__area, self.__yong = 0., 0.
        # sectional area and Young's modulus
        self.__delt, self.__epsl, self.__sigm, self.__axfc = 0., 0., 0., 0.
        # stretch, tensile strain, tensile stress, and axial force
        self.set_truss_member(area=area, yong=yong, cnv=cnv )
    ## --- section_b: (GMTrussMember) setting functions --- ##
    def set_truss_member(self,
            area: float = None, yong: float = None,
            delt: float = None, epsl: float = None,
            sigm: float = None, axfc: float = None,
            cnv: bool = True ) -> None:
        if area is not None:
            self.__area = area * 1e-4 if cnv else area  # (cm^2)
        if yong is not None:
            self.__yong = yong * 1e+9 if cnv else yong  # (kN/mm^2)
        if delt is not None:
            self.__delt = delt * 1e-3 if cnv else delt  # (mm)
        if epsl is not None:
            self.__epsl = epsl * 1e-3 if cnv else epsl  # (1/1000)
        if sigm is not None:
            self.__sigm = sigm * 1e+3 if cnv else sigm  # (kN/m^2)
        if axfc is not None:
            self.__sigm = axfc * 1e+3 if cnv else axfc  # (kN)
    ## --- section_c: (GMTrussMember) getting functions --- ##
    def area(self, cnv: bool = True) -> float:
        return self.__area / 1e-4 if cnv else self.__area  # (cm^2)
    def yong(self, cnv: bool = True) -> float:
        return self.__yong / 1e+9 if cnv else self.__yong  # (kN/mm^2)
    def delt(self, cnv: bool = True) -> float:
        return self.__delt / 1e-3 if cnv else self.__delt  # (mm)
    def epsl(self, cnv: bool = True) -> float:
        return self.__epsl / 1e-3 if cnv else self.__epsl  # (1/1000)
    def sigm(self, cnv: bool = True) -> float:
        return self.__sigm / 1e+3 if cnv else self.__sigm  # (kN/m^2)
    def axfc(self, cnv: bool = True) -> float:
        return self.__axfc / 1e+3 if cnv else self.__axfc  # (kN)
    ## --- section_d: (GMTrussMember) string function for print() --- ##
    def __str__(self) -> str:
        st = (
            f'leng (m) = {self.leng():g}, dirc (deg) = {self.dirc():g}, \n'
            f'area (cm^2) = {self.area():g}, yong (kN/mm^2) = {self.yong():g} \n'
            f'delt (mm) = {self.delt():g}, epsl (1/1000) = {self.epsl():g}, '
            f'sigm (kN/m^2) = {self.sigm():g}, axfc (kN) = {self.axfc():g} ' )
        return st
    def printclass(self, idx: str = '') -> None:
        print(idx + ':: GMTrussMember ::')
        print(self.__str__())
        self._nodea.printclass('nodea -> ')
        self._nodeb.printclass('nodeb -> ')
    ## --- section_e: (GMTrussMember) functions for properties --- ##
    def copy(self) -> object:
        return copy.deepcopy(self)
    def locn(self) -> ndarray:  # list of location numbers
        return append(self._nodea.locn(), self._nodeb.locn())
    def leng(self, cnv: bool = False) -> float:  # length (m)
        return self._nodea.dist2pint(self._nodeb, cnv=cnv)
    def dirc(self, deg: bool = False) -> float:  # direction (m)
        return self._nodea.dirc2pint(self._nodeb, deg=deg)
    def unitvect_na(self) -> ndarray:  # unit vector
        return self._nodeb.unitvect2pint(self._nodea)
    def unitvect_nb(self) -> ndarray:  # unit vector
        return self._nodea.unitvect2pint(self._nodeb)
    def unitvect(self) -> ndarray:  # unit vector
        return append(self.unitvect_na(),self.unitvect_nb())
    def calc_stiffness(self) -> ndarray:  # building stiffness matrix
        unitvect = self.unitvect()
        stif = ( outer(unitvect, unitvect)
            * self.__yong * self.__area / self.leng(False) )
        return stif
    ## --- section_f: (GMTrussMember) calculating behavior --- ##
    def calc_stretch(self) -> None:  # calculating stretch
        unitvect = self.unitvect()
        self.__delt = (
            + inner(self.unitvect_na(), self._nodea._disp.xxyy(False))
            + inner(self.unitvect_nb(), self._nodeb._disp.xxyy(False)) )
        self.__epsl = self.__delt / self.leng(False)
        self.__sigm = self.__epsl * self.__yong
        self.__axfc = self.__sigm * self.__area
        self._nodea._rafc.add(self.unitvect_na() * self.__axfc)
        self._nodeb._rafc.add(self.unitvect_nb() * self.__axfc)

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMTrussMember) main process --- ###")
    ## --- section_m0: (GMTrussMember) setting nodes and members --- ##
    node_0 = GMTrussNode(xxyy=(0., 0.), fixc=(True, True), locn=(0, 1))
    node_1 = GMTrussNode(xxyy=(0., 1.), fixc=(False, False), locn=(2, 3))
    node_1._disp.set_vector(xxyy=(1., 0.))
    node_2 = GMTrussNode(xxyy=(1., 0.), fixc=(True, True), locn=(4, 5))
    # ---------------------------------------------------------
    memb_0 = GMTrussMember(nodea=node_0, nodeb=node_1)
    memb_1 = GMTrussMember(nodea=node_1, nodeb=node_2)
    ## --- section_mb: (GMTrussMember) calculating truss member --- ##
    print(f'{memb_0.locn() = }')
    print(f'{memb_0.unitvect() = }')
    # print(f'{memb_0.calc_stiffness() = }')
    memb_0.calc_stretch()
    memb_0.printclass('memb_0 -> ')
    # ---------------------------------------------------------
    print(f'{memb_1.locn() = }')
    print(f'{memb_1.unitvect() = }')
    # print(f'{memb_1.calc_stiffness() = }')
    memb_1.calc_stretch()
    memb_1.printclass('memb_1 -> ')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussMember) class for truss member ***
      *** class GMTrussNode is embedded as nodea and nodeb ***
    ### --- section_module: (GMTrussMember) importing items from module --- ##
    *** (GMTrussNode) class for truss node ***
       *** class GMPoint is inherited; class GMVector is embedded as vect ***
    ### --- section_module: (GMTrussNode) importing items from module --- ###
    *** (GMPoint) class for point ***
       *** class GMVector is inherited ***
    ### --- section_module: (GMPoint) importing items from module --- ###
    *** (GMVector) class for vector ***
    ### --- section_module: (GMVector) importing items from module --- ###
    ### --- section_class: (GMVector) declaring class --- ###
    ### --- section_a: (GMPoint) declaring class --- ###
    ### --- section_class: (GMTrussNode) declaring class --- ###
    ### --- section_class: (GMTrussMember) declaring class --- ###
    ### --- section_main: creating class instances --- ###
    memb_0.unitvect() = array([ 0., -1.,  0.,  1.])
    memb_0.locn() = array([0, 1, 2, 3])
    memb_0.calc_stiffness() = array([
           [ 0.00e+00, -0.00e+00,  0.00e+00,  0.00e+00],
           [-0.00e+00,  2.05e+08, -0.00e+00, -2.05e+08],
           [ 0.00e+00, -0.00e+00,  0.00e+00,  0.00e+00],
           [ 0.00e+00, -2.05e+08,  0.00e+00,  2.05e+08]])
    memb_a -> :: GMTrussMember ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = 0, epsl (1/1000) = 0, sigm (kN/m^2) = 0, axfc (kN) = 0 
    nodea -> :: GMTrussNode ::
      (super) GMPoint: (m): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1
      fixc: ndarray:[ True  True]   locn: ndarray:[0 1]
      disp: GMVector: (mm): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 0.001
      exfc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
      rafc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
    nodeb -> :: GMTrussNode ::
      (super) GMPoint: (m): (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unit = 1
      fixc: ndarray:[False False]   locn: ndarray:[2 3]
      disp: GMVector: (mm): (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unit = 0.001
      exfc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
      rafc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
    memb_1.unitvect() = array([-0.70710678,  0.70710678,  0.70710678, -0.70710678])
    memb_1.locn() = array([2, 3, 4, 5])
    memb_1.calc_stiffness() = array([
           [ 72478445.0716211, -72478445.0716211, -72478445.0716211, 72478445.0716211],
           [-72478445.0716211,  72478445.0716211,  72478445.0716211, -72478445.0716211],
           [-72478445.0716211,  72478445.0716211,  72478445.0716211, -72478445.0716211],
           [ 72478445.0716211, -72478445.0716211, -72478445.0716211, 72478445.0716211]])
    memb_b -> :: GMTrussMember ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = -0.707107, epsl (1/1000) = -0.5, sigm (kN/m^2) = -102500, axfc (kN) = -102.5 
    nodea -> :: GMTrussNode ::
      (super) GMPoint: (m): (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unit = 1
      fixc: ndarray:[False False]   locn: ndarray:[2 3]
      disp: GMVector: (mm): (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unit = 0.001
      exfc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
      rafc: GMVector: (kN): (xx,yy) = (72.4784, -72.4784) : (rr,th) = (102.5, -45) : unit = 1000
    nodeb -> :: GMTrussNode ::
      (super) GMPoint: (m): (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unit = 1
      fixc: ndarray:[ True  True]   locn: ndarray:[4 5]
      disp: GMVector: (mm): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 0.001
      exfc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
      rafc: GMVector: (kN): (xx,yy) = (-72.4784, 72.4784) : (rr,th) = (102.5, 135) : unit = 1000
    '''
