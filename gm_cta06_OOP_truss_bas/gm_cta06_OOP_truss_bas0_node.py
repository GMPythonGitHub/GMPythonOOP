# gm_cta06_OOP_truss_bas0_node.py: coded by Kinya MIURA 230520
# ---------------------------------------------------------
print("*** (GMTrussNodeBasic) class for truss node ***")
# ---------------------------------------------------------
print("### --- section__: (GMTrussNodeBasic) importing items from module --- ###")
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2)

# =========================================================
print("### --- section_a: (GMTrussNodeBasic) declaring class --- ###")
class GMTrussNodeBasic():
    ## --- section_b: (GMTrussNodeBasic) initializing class instance --- ##
    def __init__(self,
            pos: tuple = (0., 0.),
            fxc: tuple = (False, False), lcn: tuple = (0, 1) ):
        self.pos, self.fxc, self.lcn = list(pos), list(fxc), list(lcn)
        # position (m), fixity condition (bool), location in matrix equation (int)
        self.dsp, self.efc = [0., 0.], [0., 0.]
        # displacement (m), external force (N)
    ## --- section_c: (GMTrussNodeBasic) string function for print() --- ##
    def __str__(self):
        st = (
            f'pos(m) = {self.pos}, fxc = {self.fxc}, lcn = {self.lcn} \n'
            f'dsp(m) = {self.dsp}, efc(N) = {self.efc}' )
        return st
    ## --- section_d: (GMTrussNodeBasic) functions calculating nodes --- ##
    def post2node(self, node: object)-> list:  # position to node
        return [node.pos[0]-self.pos[0], node.pos[1]-self.pos[1]]
    def dist2node(self, node: object) -> float:  # distance to node
        post = self.post2node(node)
        return sqrt(square(post[0])+square(post[1]))
    def dirc2node(self, node: object) -> float:  # direction to node
        post = self.post2node(node)
        return atan2(post[1],post[0])
    def unitvect2node(self, node: object) -> list:  # unit vector to node
        dirc = self.dirc2node(node)
        return [cos(dirc), sin(dirc)]

# =========================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("### --- section_m: main process --- ###")
    ## --- section_ma: (GMTrussNodeBasic) creating class instances --- ##
    nodea = GMTrussNodeBasic(pos=(0., 0.), fxc=(False, False), lcn=(0, 1))
    nodea.dsp, nodea.efc = list((0., 1.*0.001)), list((10.*1000., 0.))
    nodeb = GMTrussNodeBasic(pos=(1., 1.), fxc=(False, False), lcn=(0, 1))
    nodeb.dsp, nodeb.efc = list((0., 2.*0.001)), list((20.*1000., 0.))
    print('nodea : '); print(nodea)
    print('nodeb : '); print(nodeb)
    ## --- section_mb: (GMTrussNodeBasic) calculating node to node --- ##
    print(f'{nodea.post2node(nodeb) = }')
    print(f'{nodea.dist2node(nodeb) = }')
    print(f'{nodea.dirc2node(nodeb) = }')
    print(f'{nodea.unitvect2node(nodeb) = }')
    print(f'{nodeb.post2node(nodea) = }')
    print(f'{nodeb.dist2node(nodea) = }')
    print(f'{nodeb.dirc2node(nodea) = }')
    print(f'{nodeb.unitvect2node(nodea) = }')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussNodeBasic) class for truss node ***
    ### --- section__: (GMTrussNodeBasic) importing items from module --- ###
    ### --- section_a: (GMTrussNodeBasic) declaring class --- ###
    ### --- section_m: main process --- ###
    nodea : 
    pos(m) = [0.0, 0.0], fxc = [False, False], lcn = [0, 1] 
    dsp(m) = [0.0, 0.001], efc(N) = [10000.0, 0.0]
    nodeb : 
    pos(m) = [1.0, 1.0], fxc = [False, False], lcn = [0, 1] 
    dsp(m) = [0.0, 0.002], efc(N) = [20000.0, 0.0]
    nodea.post2node(nodeb) = [1.0, 1.0]
    nodea.dist2node(nodeb) = 1.4142135623730951
    nodea.dirc2node(nodeb) = 0.7853981633974483
    nodea.unitvect2node(nodeb) = [0.7071067811865476, 0.7071067811865476]
    nodeb.post2node(nodea) = [-1.0, -1.0]
    nodeb.dist2node(nodea) = 1.4142135623730951
    nodeb.dirc2node(nodea) = -2.356194490192345
    nodeb.unitvect2node(nodea) = [-0.7071067811865475, -0.7071067811865476]
    '''
