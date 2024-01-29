# gm_cta06_OOP_truss_bas1_member.py: coded by Kinya MIURA 230520
# ---------------------------------------------------------
print("*** (GMTrussMemberBasic) class for truss member ***")
# ---------------------------------------------------------
print("### --- section__: (GMTrussMemberBasic) importing items from module --- ###")
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2)
from gm_cta06_OOP_truss_bas0_node import GMTrussNodeBasic

# =========================================================
print("### --- section_a: (GMTrussMemberBasic) declaring class --- ###")
class GMTrussMemberBasic():
    ## --- section_b: (GMTrussMemberBasic) initializing class instance --- ##
    def __init__(self,
        nodea: GMTrussNodeBasic, nodeb: GMTrussNodeBasic,
        ara: float = 10.e-4, yng: float = 205.e9 ):
        self.nodea, self.nodeb = nodea, nodeb
        self.ara, self.yng = ara, yng
        # sectional area (m^2), Young's modulus (N/m^2)
        self.lng, self.tht = 0., 0.
        # length (m), direction angle (rad)
        self.dlt, self.eps = 0., 0.
        # strech (m), tensile strain ( )
        self.sgm, self.afc = 0., 0.
        # tensile stress (N/m^2), axial force (N)
    ## --- section_c: (GMTrussMemberBasic) string function for print() --- ##
    def __str__(self):
        st = (
            f'ara(m^2) = {self.ara:.3g}, yng(N/m^2) = {self.yng:.3g}, '
            f'lng(m) = {self.lng:.3g}, tht(deg) = {self.tht:.3g} \n'
            f'dlt(m) = {self.dlt:.3g}, eps( ) = {self.eps:.3g}, '
            f'sgm(N/m^2) = {self.sgm:.3g}, afc(N) = {self.afc:.3g}')
        return st
    ## --- section_d: (GMTrussMemberBasic) functions for  properties --- ##
    def calc_geometry(self) -> None:  # calculating geometry
        self.lng = self.nodea.dist2node(self.nodeb)
        self.tht = self.nodea.dirc2node(self.nodeb)
    def lcn(self) -> list:  # vector of location number
        return self.nodea.lcn + self.nodeb.lcn
    def stiffness(self) -> list:  # stiffness
        co, sn = self.nodeb.unitvect2node(self.nodea)
        cof = self.yng * self.ara / self.lng
        stf = [
            [+co*co*cof, +co*sn*cof, -co*co*cof, -co*sn*cof],
            [+sn*co*cof, +sn*sn*cof, -sn*co*cof, -sn*sn*cof],
            [-co*co*cof, -co*sn*cof, +co*co*cof, +co*sn*cof],
            [-sn*co*cof, -sn*sn*cof, +sn*co*cof, +sn*sn*cof] ]
        return stf
    ## --- section_e: (GMTrussMemberBasic) functions for behavior --- ##
    def calc_stretch(self) -> None:  # calculating stretch
        unitvect_nodea = self.nodeb.unitvect2node(self.nodea)
        unitvect_nodeb = self.nodea.unitvect2node(self.nodeb)
        self.dlt = (
            + self.nodea.dsp[0] * unitvect_nodea[0]
            + self.nodea.dsp[1] * unitvect_nodea[1]
            + self.nodeb.dsp[0] * unitvect_nodeb[0]
            + self.nodeb.dsp[1] * unitvect_nodeb[1] )
        self.eps = self.dlt / self.lng
        self.sgm = self.eps * self.yng
        self.afc = self.sgm * self.ara

# =========================================================
if __name__ == '__main__':
    print("### --- (GMTrussMemberBasic) section_m: main process ---")
    ## --- (GMTrussMemberBasic) section_ma: creating class instances --- ##
    nodea = GMTrussNodeBasic(
        pos=(0., 0.), fxc=(False, False), lcn=(0, 1))
    nodea.dsp, nodea.efc = [0., 1.*0.001], [10.*1000., 0.]
    nodeb = GMTrussNodeBasic(
        pos=(0., 1.), fxc=(False, False), lcn=(2, 3))
    nodeb.dsp, nodeb.efc = [0., 2.*0.001], [20.*1000., 0.]
    print('nodea : '); print(nodea)
    print('nodeb : '); print(nodeb)

    memb = GMTrussMemberBasic(
        nodea, nodeb, ara=10.e-4, yng=205.e9 )  # (cm^2), (kN/mm^2)
    print('memb : '); print(memb)

    ## --- (GMTrussMemberBasic) section_mb: calculating member --- ##
    memb.calc_geometry()
    memb.calc_stretch()
    print('memb : '); print(memb)
    print(f'{memb.stiffness() = }')
    print(f'{memb.lcn() = }')

    # =========================================================
    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussMemberBasic) class for truss member ***
    ### --- section__: (GMTrussMemberBasic) importing items from module --- ###
    *** (GMTrussNodeBasic) class for truss node ***
    ### --- section__: (GMTrussNodeBasic) importing items from module --- ###
    ### --- section_a: (GMTrussNodeBasic) declaring class --- ###
    ### --- section_a: (GMTrussMemberBasic) declaring class --- ###
    ### --- (GMTrussMemberBasic) section_m: main process ---
    nodea : 
    pos(m) = [0.0, 0.0], fxc = [False, False], lcn = [0, 1] 
    dsp(m) = [0.0, 0.001], efc(N) = [10000.0, 0.0]
    nodeb : 
    pos(m) = [0.0, 1.0], fxc = [False, False], lcn = [2, 3] 
    dsp(m) = [0.0, 0.002], efc(N) = [20000.0, 0.0]
    memb : 
    ara(m^2) = 0.001, yng(N/m^2) = 2.05e+11, lng(m) = 0, tht(deg) = 0 
    dlt(m) = 0, eps( ) = 0, sgm(N/m^2) = 0, afc(N) = 0
    memb : 
    ara(m^2) = 0.001, yng(N/m^2) = 2.05e+11, lng(m) = 1, tht(deg) = 1.57 
    dlt(m) = 0.001, eps( ) = 0.001, sgm(N/m^2) = 2.05e+08, afc(N) = 2.05e+05
    memb.stiffness() = [
        [7.68626888614202e-25, -1.255262969126037e-08, -7.68626888614202e-25, 1.255262969126037e-08], 
        [-1.255262969126037e-08, 205000000.0, 1.255262969126037e-08, -205000000.0], 
        [-7.68626888614202e-25, 1.255262969126037e-08, 7.68626888614202e-25, -1.255262969126037e-08], 
        [1.255262969126037e-08, -205000000.0, -1.255262969126037e-08, 205000000.0] ]
    memb.lcn() = [0, 1, 2, 3]
    '''
