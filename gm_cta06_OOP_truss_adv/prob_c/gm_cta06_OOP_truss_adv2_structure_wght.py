# gm_cta06_OOP_truss_adv2_structure_wght.py: coded by Kinya MIURA 240530
# ---------------------------------------------------------
print("\n*** (GMTrussStructure) class for segment ***")
print("  *** class GMTrussNode, GMTrussMemberAdvanced are embedded as nodes and membs ***")
# ---------------------------------------------------------
print("### --- section_module: (GMTrussStructure) importing items from module --- ###")
from numpy import (
    array, append, zeros as zers, full, ix_,
    inner, logical_not as lognot)
from numpy.linalg import solve
from gm_cta06_OOP_truss_adv1_member_wght import (GMTrussNode, GMTrussMember)

# =========================================================
print("### --- section_class: (GMTrussStructure) declaring class --- ###")
class GMTrussStructure():
    ## --- section_a: (GMTrussStructure) initializing class instance --- ##
    def __init__(self, nodes: list, membs: list):
        self._nodes, self._membs = [], []
        # lists of nodes and members
        self._fixc, self._disp, = array([]), array([])
        # fixity condition list and displacement
        self._exfc, self._wght = array([]), array([])
        # external force vectors and self weight
        self._stif = array([[]])
        # stiffness matrix
        self.set_truss_structure(nodes, membs)
    ## --- section_b: (GMTrussStructure) setting functions --- ##
    def set_truss_structure(self, nodes: list, membs: list) -> None:
        self._nodes, self._membs = nodes, membs
        degfred = len(self._nodes) * len(self._nodes[0].xxyy())
        self._fixc = full((degfred,), False)
        self._disp, self._exfc, self._wght = zers((degfred,)), zers((degfred,)), zers((degfred,))
        self._stif = zers((degfred, degfred,))
    ## --- section_c: (GMTrussStructure) getting functions --- ##
    def numnode(self) -> int: return len(self._nodes)
    def nummemb(self) -> int: return len(self._membs)
    def degfred(self) -> int: return len(self._nodes) * len(self._nodes[0].xxyy())
    ## --- section_d: (GMTrussStructure) string function --- ##
    def __str__(self):
        st  = (
            f'numnode = {self.numnode():d}, nummemb = {self.nummemb():d}, '
            f'degfred = {self.degfred():d} ' )
        return st
    def printclass(self, idx: str = '') -> None:
        print(idx + ':: GMTrussStructure ::')
        print(self.__str__())
        print('nodes[]: GMTrussNode:')
        for i, node in enumerate(self._nodes):
            node.printclass(f'**[{i:02d}]')
        print('membs[]: GMTrussMember:')
        for i, memb in enumerate(self._membs):
            memb.printclass(f'**[{i:02d}]')
    ## --- section_e: (GMTrussStructure) building matrix equation --- ##
    def buld_matrixeq(self) -> None:
        for memb in self._membs:  # building matrix
            stif = memb.calc_stiffness()
            memb.calc_weight()
            locn = memb.locn()
            for i, ilocn in enumerate(locn):
                for j, jlocn in enumerate(locn):
                    self._stif[ilocn,jlocn] += stif[i,j]
        for node in self._nodes:  # building vectors
            for (fixc,locn,disp,exfc,wght) in zip(
                    node.fixc(),node.locn(),node._disp.xxyy(False),node._exfc.xxyy(False),node._wght.xxyy(False) ):
                self._fixc[locn] = fixc
                self._disp[locn] = disp
                self._exfc[locn] = exfc
                self._wght[locn] = wght
    ## --- section_f: (GMTrussStructure) solving matrix equation --- ##
    def solv_matrixeq(self) -> None:  # solving matrix equation
        fixc, frec = self._fixc, lognot(self._fixc)  # setting workspace
        aa = self._stif[ix_(frec, frec)]
        bb = self._exfc[ix_(frec)] + self._wght[ix_(frec)] - inner(self._stif[ix_(frec, fixc)], self._disp[ix_(fixc)])
        xx = solve(aa,bb)  # solving matrix equation
        self._disp[ix_(frec)] = xx
        self._exfc = inner(self._stif, self._disp) - self._wght
        for i, node in enumerate(self._nodes):  # modifying nodes
            xxyy = []
            for locn in node.locn():
                xxyy.append(self._disp[locn])
            self._nodes[i]._disp.set_xxyy(xxyy, cnv=False)
        for memb in self._membs:
            memb.calc_stretch()
        for node in self._nodes:
            node._rafc.sub(node._wght)

    # =========================================================
    print("### --- section_g: (GMTrussStructure) drawing figure --- ###")
    def graph(self,
            scl_dfm: float = 0.05, scl_frc: float = 0.005,
            xlim: tuple =(-1.0, 2.0), ylim: tuple = (-1.0, 2.0),
            fname: str = '') -> None:
        import matplotlib.pyplot as plt
        ## --- section_g0: setting figure --- ##
        plt.rcdefaults()  # initializing drawing environment
        fig, ax = plt.subplots(figsize=(8., 6.))
        fig.suptitle('Truss Deformation Behavior Subjected to Forces')
        ax.set_aspect('equal')
        leng_lim = 1.
        ax.set_xlim(xlim); ax.set_ylim(ylim)
        ax.hlines(0., -0.5, +1.5, linestyle='-', color='black', linewidth=2.)
        ## --- section_g1: drawing reference truss frame --- ##
        for memb in self._membs:  # truss members
            xx, yy = append(
                memb._nodea.xxyy().reshape(2,1),
                memb._nodeb.xxyy().reshape(2,1), axis=1)
            ax.plot( xx, yy,
                color='0.7', linewidth=3., linestyle='-', zorder=1 )
        for node in self._nodes:  # truss nodes
            xx, yy = node.xxyy(False)
            ax.scatter( xx, yy,
                marker='o', s=120., color='1.0', linewidth=2., edgecolor='0.7',
                zorder=2 )
        ## --- section_g2: drawing deformed truss frame --- ##
        for memb in self._membs:  # truss members
            xx, yy = append(
                (memb._nodea.xxyy() + memb._nodea._disp.xxyy() * scl_dfm).reshape(2,1),
                (memb._nodeb.xxyy() + memb._nodeb._disp.xxyy() * scl_dfm ).reshape(2,1), axis=1)
            ax.plot( xx, yy,
                color='0.0', linewidth=3., linestyle='-', zorder=3 )
        for node in self._nodes:  # truss nodes and external forces
            xx, yy = node.xxyy() + node._disp.xxyy() * scl_dfm
            ax.scatter( xx, yy,
                marker='o', s=120., color='1.0', linewidth=2.0, edgecolor='0.0', zorder=4)
            dxx, dyy = node._rafc.xxyy() * scl_frc
            if abs(dxx) > leng_lim / 100. or abs(dyy) > leng_lim / 100.:
                ax.arrow( xx-dxx, yy - dyy, dxx, dyy,
                    width=0.02, length_includes_head=True, color='red', zorder=5)
        ## --- section_g3: saving and showing figure --- ##
        fig.savefig('gm_cta06_OOP_truss_adv_structure'+fname+'.png')
        plt.show()

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMTrussStructure) setting structure --- ###")
    ## --- section_m0: (GMTrussStructure) setting nodes --- ##
    nodes = list(range(4))
    leng, exfc = 1., 100.  # (m), (kN)
    nodes[0] = GMTrussNode(
        xxyy=(leng*0, leng*0), fixc=(True, True), locn=(0, 1) )
    nodes[1] = GMTrussNode(
        xxyy=(leng*1, leng*0), fixc=(True, True), locn=(2, 3) )
    nodes[2] = GMTrussNode(
        xxyy=(leng*0, leng*1), fixc=(False, False), locn=(4, 5) )
    # nodes[2]._exfc.set_vector(xxyy=(exfc, 0.))
    nodes[3] = GMTrussNode(
        xxyy=(leng*1, leng*1), fixc=(False, False), locn=(6, 7) )
    ## --- section_m1: (GMTrussStructure) setting members --- ##
    area, yong = 10., 205.  # (cm^2), (kN/mm^2)
    rhos, grac = 7900., 9.80665
    membs = list(range(4))
    membs[0] = GMTrussMember(
        nodea=nodes[0], nodeb=nodes[2], area=area, yong=yong, rhos=rhos, grac=grac)
    membs[1] = GMTrussMember(
        nodea=nodes[1], nodeb=nodes[3], area=area, yong=yong, rhos=rhos, grac=grac)
    membs[2] = GMTrussMember(
        nodea=nodes[2], nodeb=nodes[3], area=area, yong=yong, rhos=rhos, grac=grac)
    membs[3] = GMTrussMember(
        nodea=nodes[0], nodeb=nodes[3], area=area, yong=yong, rhos=rhos, grac=grac)
    ## --- section_m2: (GMTrussStructure) creating instance of structure --- ##")
    strc = GMTrussStructure(nodes=nodes, membs=membs)
    ## --- section_m3: (GMTrussStructure) building matrix equation --- ##
    strc.buld_matrixeq()
    # print(f'{strc._stif = }')
    # print(f'{strc._fixc = }')
    # print(f'{strc._disp = }')
    # print(f'{strc._exfc = }')
    ## --- section_m4: (GMTrussStructure) solving matrix equation --- ##
    strc.solv_matrixeq()
    strc.printclass('strc -> ')
    ## --- section_m5: (GMTrussStructureAdvanced) drawing figure --- ##
    strc.graph(
        scl_dfm=0.05*100, scl_frc=0.005*100, xlim=(-1.0,2.0), ylim=(-1.0, 2.0) )

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussStructure) class for segment ***
      *** class GMTrussNode, GMTrussMemberAdvanced are embedded as nodes and membsb ***
    ### --- section_module: (GMTrussStructure) importing items from module --- ###
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
    ### --- section_class: (GMPoint) declaring class --- ###
    ### --- section_class: (GMTrussNode) declaring class --- ###
    ### --- section_class: (GMTrussMember) declaring class --- ###
    ### --- section_class: (GMTrussStructure) declaring class --- ###
    ### --- section_g: (GMTrussStructure) drawing figure --- ###
    ### --- section_main: (GMTrussStructure) setting structure --- ###
    strc -> :: GMTrussStructure ::
    numnode = 4, nummemb = 4, degfred = 8 
    nodes[]: GMTrussNode:
    **[00]:: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1
      fixc = [ True  True], locn = [0 1] 
      disp: GMVector (mm): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [-100. -100.] : rrth = [ 141.42135624 -135.        ] : unit = 1000
    **[01]:: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [1. 0.] : rrth = [1. 0.] : unit = 1
      fixc = [ True  True], locn = [2 3] 
      disp: GMVector (mm): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [  0. 100.] : rrth = [100.  90.] : unit = 1000
    **[02]:: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [0. 1.] : rrth = [ 1. 90.] : unit = 1
      fixc = [False False], locn = [4 5] 
      disp: GMVector (mm): xxyy = [2.3553303 0.       ] : rrth = [2.3553303 0.       ] : unit = 0.001
      exfc: GMVector (kN): xxyy = [100.   0.] : rrth = [100.   0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [100.   0.] : rrth = [100.   0.] : unit = 1000
    **[03]:: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [1. 1.] : rrth = [ 1.41421356 45.        ] : unit = 1
      fixc = [False False], locn = [6 7] 
      disp: GMVector (mm): xxyy = [ 1.86752543 -0.48780488] : rrth = [  1.93018259 -14.6388066 ] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
    membs[]: GMTrussMember:
    **[00]:: GMTrussMember ::
    leng (m) = 1, dirc (deg) = 1.5708, 
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = 0, epsl (1/1000) = 0, sigm (kN/m^2) = 0, axfc (kN) = 0 
    nodea -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1
      fixc = [ True  True], locn = [0 1] 
      disp: GMVector (mm): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [-100. -100.] : rrth = [ 141.42135624 -135.        ] : unit = 1000
    nodeb -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [0. 1.] : rrth = [ 1. 90.] : unit = 1
      fixc = [False False], locn = [4 5] 
      disp: GMVector (mm): xxyy = [2.3553303 0.       ] : rrth = [2.3553303 0.       ] : unit = 0.001
      exfc: GMVector (kN): xxyy = [100.   0.] : rrth = [100.   0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [100.   0.] : rrth = [100.   0.] : unit = 1000
    **[01]:: GMTrussMember ::
    leng (m) = 1, dirc (deg) = 1.5708, 
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = -0.487805, epsl (1/1000) = -0.487805, sigm (kN/m^2) = -100000, axfc (kN) = -100 
    nodea -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [1. 0.] : rrth = [1. 0.] : unit = 1
      fixc = [ True  True], locn = [2 3] 
      disp: GMVector (mm): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [  0. 100.] : rrth = [100.  90.] : unit = 1000
    nodeb -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [1. 1.] : rrth = [ 1.41421356 45.        ] : unit = 1
      fixc = [False False], locn = [6 7] 
      disp: GMVector (mm): xxyy = [ 1.86752543 -0.48780488] : rrth = [  1.93018259 -14.6388066 ] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
    **[02]:: GMTrussMember ::
    leng (m) = 1, dirc (deg) = 0, 
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = -0.487805, epsl (1/1000) = -0.487805, sigm (kN/m^2) = -100000, axfc (kN) = -100 
    nodea -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [0. 1.] : rrth = [ 1. 90.] : unit = 1
      fixc = [False False], locn = [4 5] 
      disp: GMVector (mm): xxyy = [2.3553303 0.       ] : rrth = [2.3553303 0.       ] : unit = 0.001
      exfc: GMVector (kN): xxyy = [100.   0.] : rrth = [100.   0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [100.   0.] : rrth = [100.   0.] : unit = 1000
    nodeb -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [1. 1.] : rrth = [ 1.41421356 45.        ] : unit = 1
      fixc = [False False], locn = [6 7] 
      disp: GMVector (mm): xxyy = [ 1.86752543 -0.48780488] : rrth = [  1.93018259 -14.6388066 ] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
    **[03]:: GMTrussMember ::
    leng (m) = 1.41421, dirc (deg) = 0.785398, 
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = 0.97561, epsl (1/1000) = 0.68986, sigm (kN/m^2) = 141421, axfc (kN) = 141.421 
    nodea -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1
      fixc = [ True  True], locn = [0 1] 
      disp: GMVector (mm): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [-100. -100.] : rrth = [ 141.42135624 -135.        ] : unit = 1000
    nodeb -> :: GMTrussNode ::
    (GMPoint) (GMVector) xxyy = [1. 1.] : rrth = [ 1.41421356 45.        ] : unit = 1
      fixc = [False False], locn = [6 7] 
      disp: GMVector (mm): xxyy = [ 1.86752543 -0.48780488] : rrth = [  1.93018259 -14.6388066 ] : unit = 0.001
      exfc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
      rafc: GMVector (kN): xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1000
    '''
