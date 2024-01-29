# gm_cta06_OOP_truss_adv0_node.py: coded by Kinya MIURA 230524
# ---------------------------------------------------------
print("*** (GMTrussNode) class for truss node ***")
print("   *** class GMPoint is inherited; class GMVector is embedded as vect ***")
# ---------------------------------------------------------
print("### --- section_module: (GMTrussNode) importing items from module --- ###")
from numpy import (ndarray, array)
import copy
from gm_cta06_OOP_truss_1_point import (GMPoint, GMVector)

# =========================================================
print("### --- section_class: (GMTrussNode) declaring class --- ###")
class GMTrussNode(GMPoint):  # inheriting class GMPoint(GMVector)
    ## --- section_a: (GMTrussNode) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (0., 0.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True,
            fixc: tuple = (False, False), locn: tuple = (0, 1) ):
        super().__init__(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)  # (m)
        self.__fixc, self.__locn = None, None
        self._disp = GMVector(xxyy=(0., 0.), unit=1e-3)  # (mm)
        self._exfc = GMVector(xxyy=(0., 0.), unit=1e+3)  # (kN)
        self._rafc = GMVector(xxyy=(0., 0.), unit=1e+3)  # (kN)
        self.set_truss_node(fixc=fixc, locn=locn)
    ## --- section_b: (GMTrussNode) setting functions --- ##
    def set_truss_node(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True,
            fixc: tuple = None, locn: tuple = None ) -> None:
        self.set_point(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
        if fixc is not None: self.__fixc = array(fixc)
        if locn is not None: self.__locn = array(locn)
    ## --- section_c: (GMTrussNode) getting functions --- ##
    def fixc(self) -> ndarray: return self.__fixc
    def locn(self) -> ndarray: return self.__locn
    ## --- section_d: (GMTrussNode) string function for print() --- ##
    def __str__(self) -> str:
        st  = '(GMPoint) ' + super().__str__() + '\n'
        st += (
            f'  fixc = {self.__fixc}, locn = {self.__locn} ' )
        return st
    def printclass(self, idx: str = '') -> None:
        print(
            idx + ':: GMTrussNode ::\n'
            + self.__str__() + '\n'
            + '  disp: GMVector (mm): ' + self._disp.__str__() + '\n'
            + '  exfc: GMVector (kN): ' + self._exfc.__str__() + '\n'
            + '  rafc: GMVector (kN): ' + self._rafc.__str__() + '' )
    ## --- section_e: (GMTrussNode) functions for truss nodes --- ##
    def copy(self) -> object:
        return copy.deepcopy(self)

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMTrussNode) main process --- ###")
    ## --- section_ma: (GMTrussNode) setting nodes --- ##
    node_a = GMTrussNode(xxyy=(1., 2.), fixc=(True, True), locn=(0, 1))
    node_a.printclass('node_a -> ')
    node_b = GMTrussNode(xxyy=(2., 1.), fixc=(False, False), locn=(2, 3))
    node_b.printclass('node_b -> ')
    ## --- section_mb: (GMTrussNode) setting node properties --- ##
    node_c = GMTrussNode(xxyy=(2., 1.))
    node_c.set_truss_node(rrth=(1., 45.), fixc=(False,True), locn=(4, 5))
    node_c._disp.set_vector(xxyy=(1., 0.))
    node_c._exfc.set_vector(xxyy=(0., 1.))
    node_c._rafc.set_vector(xxyy=(0., 2.))
    node_c.printclass('node_c -> ')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
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
    ### --- section_main: (GMTrussNode) creating class instances --- ###
    node_a -> :: GMTrussNode ::
      (super) GMPoint: (m): (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unit = 1
      fixc: ndarray:[ True  True]   locn: ndarray:[0 1]
      disp: GMVector: (mm): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 0.001
      exfc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
      rafc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
    node_b -> :: GMTrussNode ::
      (super) GMPoint: (m): (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unit = 1
      fixc: ndarray:[False False]   locn: ndarray:[2 3]
      disp: GMVector: (mm): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 0.001
      exfc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
      rafc: GMVector: (kN): (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unit = 1000
    node_c -> :: GMTrussNode ::
      (super) GMPoint: (m): (xx,yy) = (0.707107, 0.707107) : (rr,th) = (1, 45) : unit = 1
      fixc: ndarray:[False  True]   locn: ndarray:[4 5]
      disp: GMVector: (mm): (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unit = 0.001
      exfc: GMVector: (kN): (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unit = 1000
      rafc: GMVector: (kN): (xx,yy) = (0, 2) : (rr,th) = (2, 90) : unit = 1000
     '''
