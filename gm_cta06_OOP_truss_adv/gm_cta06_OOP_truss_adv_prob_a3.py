# gm_cta06_OOP_truss_adv_prob_a3.py: coded by Kinya MIURA 240530
# ---------------------------------------------------------
print("\n*** (GMTrussStructure) class for segment ***")
print("  *** class GMTrussNode, GMTrussMemberAdvanced are embedded as nodes and membsb ***")
# ---------------------------------------------------------
print("### --- section_module: (GMTrussStructure) importing items from module --- ###")
from gm_cta06_OOP_truss_adv2_structure import (
    GMTrussNode, GMTrussMember, GMTrussStructure )

# =========================================================

print("### --- section_main: (GMTrussStructure) setting structure --- ###")

nstry = 2  # number of stories

## --- section_ma: (GMTrussStructure) setting list of nodes --- ##
nodes = list(range(2 + 2 * nstry))
leng, exfc = 1., 100.  # (m), (kN)
nodes[0] = GMTrussNode(
    xxyy=(leng * 0, leng * 0), fixc=(True, True), locn=(0, 1))
nodes[1] = GMTrussNode(
    xxyy=(leng * 1, leng * 0), fixc=(True, True), locn=(2, 3))
for istry in range(nstry):
    nodeo = 2 + 2 * istry
    nodes[nodeo+0] = GMTrussNode(
        xxyy=(leng*0, leng*(istry+1)),
        fixc=(False, False), locn=(nodeo*2+0, nodeo*2+1) )
    nodes[nodeo+1] = GMTrussNode(
        xxyy=(leng*1, leng*(istry+1)),
        fixc=(False, False), locn=(nodeo*2+2, nodeo*2+3) )
nodes[nstry*2]._exfc.set_vector(xxyy=(exfc, 0.))

## --- section_mb: (GMTrussStructure) setting list of members --- ##
membs = list(range(5 * nstry))  # list of truss members
area, yong = 10., 205.  # (cm^2), (kN/mm^2
for istry in range(nstry):
    nodeo, membo = 2 + 2 * istry, 5 * istry
    membs[membo+0] = GMTrussMember(
        nodea=nodes[nodeo-2], nodeb=nodes[nodeo+0], area=area, yong=yong)
    membs[membo+1] = GMTrussMember(
        nodea=nodes[nodeo-1], nodeb=nodes[nodeo+1], area=area, yong=yong)
    membs[membo+2] = GMTrussMember(
        nodea=nodes[nodeo+0], nodeb=nodes[nodeo+1], area=area, yong=yong)
    membs[membo+3] = GMTrussMember(
        nodea=nodes[nodeo-2], nodeb=nodes[nodeo+1], area=area, yong=yong)
    membs[membo+4] = GMTrussMember(
        nodea=nodes[nodeo-1], nodeb=nodes[nodeo+0], area=area, yong=yong)

## --- section_mc: (GMTrussStructure) creating instance of structure --- ##")
strc = GMTrussStructure(nodes=nodes, membs=membs)

## --- section_md: (GMTrussStructure) building and solving matrix equation --- ##
strc.buld_matrixeq()
strc.solv_matrixeq()
strc.printclass('strc -> ')

## --- section_me: (GMTrussStructureAdvanced) drawing figure --- ##
strc.graph(
    scl_dfm=0.05/nstry, scl_frc=0.005/nstry,
    xlim=(-1.0,1+nstry), ylim=(-1.0, 1+nstry) )

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
