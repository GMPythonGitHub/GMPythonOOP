# gm_cta06_OOP_truss_adv_prob_b2.py: coded by Kinya MIURA 240530
# ---------------------------------------------------------
print("\n*** (GMTrussStructure) class for segment ***")
print("  *** class GMTrussNode, GMTrussMemberAdvanced are embedded as nodes and membs ***")
# ---------------------------------------------------------
print("### --- section_module: (GMTrussStructure) importing items from module --- ###")
from gm_cta06_OOP_truss_adv2_structure import (
    GMTrussNode, GMTrussMember, GMTrussStructure )

# =========================================================

print("### --- section_main: (GMTrussStructure) setting structure --- ###")

nsect = 4  # number of stories

## --- section_ma: (GMTrussStructure) setting list of nodes --- ##
nodes = list(range(2 + 2 * nsect))
leng, exfc = 1., 100.  # (m), (kN)
dltth = 180 // 4
nodes[0] = GMTrussNode(rrth=(leng*1, 0), fixc=(True, True), locn=(0, 1))  # nodes on the ground
nodes[1] = GMTrussNode(rrth=(leng*2, 0), fixc=(True, True), locn=(2, 3))
for isect in range(nsect):  # n-section nodes
    nodeo = 2 * isect  # initial node number
    if isect < nsect-1:
        nodes[nodeo+2] = GMTrussNode(rrth=(leng*1, dltth*(isect+1)), fixc=(False, False), locn=(nodeo*2+4, nodeo*2+5))
        nodes[nodeo+3] = GMTrussNode(rrth=(leng*2, dltth*(isect+1)), fixc=(False, False), locn=(nodeo*2+6, nodeo*2+7))
    else:
        nodes[nodeo+2] = GMTrussNode(rrth=(leng*1, dltth*(isect+1)), fixc=(True, True), locn=(nodeo*2+4, nodeo*2+5))
        nodes[nodeo+3] = GMTrussNode(rrth=(leng*2, dltth*(isect+1)), fixc=(True, True), locn=(nodeo*2+6, nodeo*2+7))
nodes[nsect//2*2+1]._exfc.set_vector(xxyy=(exfc, 0.))  # external force

## --- section_mb: (GMTrussStructure) setting list of members --- ##
membs = list(range(5 * nsect - 1))  # list of truss members
area, yong = 10., 205.  # (cm^2), (kN/mm^2)
for isect in range(nsect):  # n-section membs
    nodeo = 2 * isect  # initial node number
    membo = 5 * isect  # initial member number
    membs[membo+0] = GMTrussMember(nodea=nodes[nodeo+0], nodeb=nodes[nodeo+2], area=area, yong=yong)
    membs[membo+1] = GMTrussMember(nodea=nodes[nodeo+1], nodeb=nodes[nodeo+3], area=area, yong=yong)
    membs[membo+2] = GMTrussMember(nodea=nodes[nodeo+0], nodeb=nodes[nodeo+3], area=area, yong=yong)
    membs[membo+3] = GMTrussMember(nodea=nodes[nodeo+1], nodeb=nodes[nodeo+2], area=area, yong=yong)
    if isect < nsect-1:
        membs[membo+4] = GMTrussMember(nodea=nodes[nodeo+2], nodeb=nodes[nodeo+3], area=area, yong=yong)

## --- section_mc: (GMTrussStructure) creating instance of structure --- ##")
strc = GMTrussStructure(nodes=nodes, membs=membs)

## --- section_md: (GMTrussStructure) building and solving matrix equation --- ##
strc.buld_matrixeq()
strc.solv_matrixeq()
strc.printclass('strc -> ')

## --- section_me: (GMTrussStructureAdvanced) drawing figure --- ##
strc.graph(
    scl_dfm=0.05/1, scl_frc=0.005/1,
    xlim=(-1-2,1+2), ylim=(-1-1, 1+3), fname='_b2' )

## --- section_me: (GMTrussStructureAdvanced) finding max and min values --- ##
print()
dispxs = []
for node in nodes:
    dispxs.append(node._disp.xxyy(True)[0])
dispxmax = max(dispxs); dispxmaxidx = dispxs.index(dispxmax)
print(f'{dispxmax = }: {dispxmaxidx = }')

# axial force
print()
axfcs = []
for memb in membs:
    axfcs.append(memb.axfc(True))
# axfcs = [memb.axfc() for memb in membs]
axfcmax = max(axfcs); axfcmaxidx = axfcs.index(axfcmax)
print(f'{axfcmax = }: {axfcmaxidx = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
'''
