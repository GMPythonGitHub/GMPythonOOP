# gm_cta06_basic_a_truss_member.py: coded by Kinya MIURA 230520
# ---------------------------------------------------------
print("*** (GMTrussStructureBasic) class for truss structure ***")
# ---------------------------------------------------------
print("### --- section__: (GMTrussStructureBasic) importing items from module --- ###")
from numpy.linalg import solve
from gm_cta06_OOP_truss_bas0_node import GMTrussNodeBasic
from gm_cta06_OOP_truss_bas1_member import GMTrussMemberBasic

# =========================================================
print("### --- section_class: (GMTrussStructureBasic) declaring class --- ##")
class GMTrussStructureBasic():
    ## --- section_a: (GMTrussStructureBasic) initializing class instance ---")
    def __init__(self, nnode: int, nmemb: int):
        self.nnode, self.nmemb, self.dfrd = nnode, nmemb, nnode * 2
        # number of nodes, number of members, degree of freedom
        self.nodes, self.membs = [], []
        # list of nodes, list of members
        self.stif = []
        # global striffness matrix
        self.dsp, self.efc, self.fxc = [], [], []
        # global vectors of displacement, external force, fixity condition
    ## --- section_b: (GMTrussStructureBasic) string function for print() --- ##
    def __str__(self):
        st = (
            f'nnode = {self.nnode:g}, nmemb = {self.nmemb:g}, '
            f'nmdfrd = {self.nmemb:g}' )
        return st
    ## --- section_c: (GMTrussStructureBasic) building ans solving matrix equation --- ##
    def buld_mtxeq(self) -> None:
        # setting work space
        for i in range(self.nmemb):
            self.membs[i].calc_geometry()
        self.stf = [[0.] * self.dfrd for i in range(self.dfrd)]
        self.dsp, self.efc = [0.] * self.dfrd, [0.] * self.dfrd
        self.fxc = [False] * self.dfrd
        # building global matrix
        for memb in self.membs:
            stf = memb.stiffness()
            lcn = memb.lcn()
            for j in range(2 * 2):
                for k in range(2 * 2):
                    self.stf[lcn[j]][lcn[k]] += stf[j][k]
        # building global vectors
        for node in self.nodes:
            for i in range(2):
                self.dsp[node.lcn[i]] = node.dsp[i]
                self.efc[node.lcn[i]] = node.efc[i]
                self.fxc[node.lcn[i]] = node.fxc[i]
    def solv_mtxeq(self) -> None:
        # setting work space
        wks = 0
        for fxc in self.fxc:
            if not fxc: wks += 1
        aa = [[0.] * wks for i in range(wks)]
        bb = [0.] * wks
        # setting working matrix
        ii = 0
        for i in range(self.dfrd):
            if not self.fxc[i]:
                jj = 0
                for j in range(self.dfrd):
                    if not self.fxc[j]:
                        aa[ii][jj] = self.stf[i][j]
                        jj += 1
                ii += 1
        # setting working vector
        ii = 0
        for i in range(self.dfrd):
            if not self.fxc[i]:
                bb[ii] = self.efc[i]
                for j in range(self.dfrd):
                    if self.fxc[j]:
                        bb[ii] -= self.stf[i][j] * self.dsp[j]
                ii += 1
        # solving matrix equation
        xx = list(solve(aa, bb))
        ii = 0
        for i in range(self.dfrd):
            if not self.fxc[i]:
                self.dsp[i] = xx[ii]
                ii += 1
        for i in range(self.dfrd):
            self.efc[i] = 0
            for j in range(self.dfrd):
                self.efc[i] += self.stf[i][j] * self.dsp[j]
        # calculating truss nodes
        for i in range(self.nnode):
            for j in range(2):
                self.nodes[i].dsp[j] = self.dsp[self.nodes[i].lcn[j]]
                self.nodes[i].efc[j] = self.efc[self.nodes[i].lcn[j]]
        for i in range(self.nmemb):
            self.membs[i].calc_stretch()

# =========================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("### --- section_main: (GMTrussStructureBasic) creating class instances --- ###")
    ## --- section_ma: (GMTrussStructureBasic) creating class instance ---
    nnode, nmemb = 4, 4
    struc = GMTrussStructureBasic(nnode,nmemb)
    ## --- section_mb: (GMTrussStructureBasic) generating list of nodes ---
    nodes = list(range(nnode))
    efc = 100.*1000.
    nodes[0] = GMTrussNodeBasic(
        pos=(0.,0.), lcn=(0,1), fxc=(True,True) )
    nodes[1] = GMTrussNodeBasic(
        pos=(1.,0.), lcn=(2,3), fxc=(True,True) )
    nodes[2] = GMTrussNodeBasic(
        pos=(0.,1.), lcn=(4,5), fxc=(False,False) )
    nodes[3] = GMTrussNodeBasic(
        pos=(1.,1.), lcn=(6,7), fxc=(False,False) )
    nodes[2].efc[0] = efc
    struc.nodes = nodes
    ## --- section_mc: (GMTrussStructureBasic) generating list of membes --- ##
    membs = list(range(nmemb))
    ara, yng = 10. * 1.e-4, 205. * 1.e9
    membs[0] = GMTrussMemberBasic(
        nodea=nodes[0], nodeb=nodes[2], ara=ara, yng=yng)
    membs[1] = GMTrussMemberBasic(
        nodea=nodes[1], nodeb=nodes[3], ara=ara, yng=yng)
    membs[2] = GMTrussMemberBasic(
        nodea=nodes[2], nodeb=nodes[3], ara=ara, yng=yng)
    membs[3] = GMTrussMemberBasic(
        nodea=nodes[0], nodeb=nodes[3], ara=ara, yng=yng)
    struc.membs = membs
    ## --- section_md: (GMTrussStructureBasic) solving matrix equation --- ##
    struc.buld_mtxeq()
    struc.solv_mtxeq()
    ## --- section_me: (GMTrussStructureBasic) printing results --- ##
    print('stuc : '); print(struc)
    print()
    for i in range(nnode):
        print(f'nodes[{i:d}] '); print(nodes[i])
    print()
    for i in range(nmemb):
        print(f'membs[{i:d}] '); print(membs[i])

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussStructureBasic) class for truss structure ***
    ### --- section__: (GMTrussStructureBasic) importing items from module --- ###
    *** (GMTrussNodeBasic) class for truss node ***
    ### --- section__: (GMTrussNodeBasic) importing items from module --- ###
    ### --- section_class: (GMTrussNodeBasic) declaring class --- ###
    *** (GMTrussMemberBasic) class for truss member ***
    ### --- section__: (GMTrussMemberBasic) importing items from module --- ###
    ### --- section_class: (GMTrussMemberBasic) declaring class --- ###
    ### --- section_class: (GMTrussStructureBasic) declaring class --- ##
    ### --- section_main: (GMTrussStructureBasic) creating class instances --- ###
    stuc : 
    nnode = 4, nmemb = 4, nmdfrd = 4
    
    nodes[0] 
    pos(m) = [0.0, 0.0], fxc = [True, True], lcn = [0, 1] 
    dsp(m) = [0.0, 0.0], efc(N) = [-99999.99999999996, -99999.99999999997]
    nodes[1] 
    pos(m) = [1.0, 0.0], fxc = [True, True], lcn = [2, 3] 
    dsp(m) = [0.0, 0.0], efc(N) = [-6.123233995736765e-12, 100000.0]
    nodes[2] 
    pos(m) = [0.0, 1.0], fxc = [False, False], lcn = [4, 5] 
    dsp(m) = [0.0023553303047542384, 2.039612541836923e-19], efc(N) = [99999.99999999993, 7.962108318232385e-27]
    nodes[3] 
    pos(m) = [1.0, 1.0], fxc = [False, False], lcn = [6, 7] 
    dsp(m) = [0.0018675254267054582, -0.0004878048780487803], efc(N) = [3.637978807091713e-11, 0.0]
    
    membs[0] 
    ara(m^2) = 0.001, yng(N/m^2) = 2.05e+11, lng(m) = 1, tht(deg) = 1.57 
    dlt(m) = 3.48e-19, eps( ) = 3.48e-19, sgm(N/m^2) = 7.14e-08, afc(N) = 7.14e-11
    membs[1] 
    ara(m^2) = 0.001, yng(N/m^2) = 2.05e+11, lng(m) = 1, tht(deg) = 1.57 
    dlt(m) = -0.000488, eps( ) = -0.000488, sgm(N/m^2) = -1e+08, afc(N) = -1e+05
    membs[2] 
    ara(m^2) = 0.001, yng(N/m^2) = 2.05e+11, lng(m) = 1, tht(deg) = 0 
    dlt(m) = -0.000488, eps( ) = -0.000488, sgm(N/m^2) = -1e+08, afc(N) = -1e+05
    membs[3] 
    ara(m^2) = 0.001, yng(N/m^2) = 2.05e+11, lng(m) = 1.41, tht(deg) = 0.785 
    dlt(m) = 0.000976, eps( ) = 0.00069, sgm(N/m^2) = 1.41e+08, afc(N) = 1.41e+05
    '''
