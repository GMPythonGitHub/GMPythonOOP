# gm_cta06_OOP_truss_adv_prob_b1.py: coded by Kinya MIURA 240530
# ---------------------------------------------------------
print("\n*** (GMTrussStructure) class for segment ***")
print("  *** class GMTrussNode, GMTrussMemberAdvanced are embedded as nodes and membs ***")
# ---------------------------------------------------------
print("### --- section_module: (GMTrussStructure) importing items from module --- ###")
from numpy import (cos, sin, pi)
from gm_cta06_OOP_truss_adv2_structure import (
    GMTrussNode, GMTrussMember, GMTrussStructure )

# =========================================================

print("### --- section_main: (GMTrussStructure) setting structure --- ###")

## --- section_ma: (GMTrussStructure) setting list of nodes --- ##
nodes = list(range(10))
leng, exfc = 1., 100.  # (m), (kN)
nodes[0] = GMTrussNode(xxyy=(leng*1*cos(pi/4*0), leng*1*sin(pi/4*0)), fixc=(True, True), locn=(0, 1))
nodes[1] = GMTrussNode(xxyy=(leng*2*cos(pi/4*0), leng*2*sin(pi/4*0)), fixc=(True, True), locn=(2, 3))
nodes[2] = GMTrussNode(xxyy=(leng*1*cos(pi/4*1), leng*1*sin(pi/4*1)), fixc=(False, False), locn=(4, 5))
nodes[3] = GMTrussNode(xxyy=(leng*2*cos(pi/4*1), leng*2*sin(pi/4*1)), fixc=(False, False), locn=(6, 7))
nodes[4] = GMTrussNode(xxyy=(leng*1*cos(pi/4*2), leng*1*sin(pi/4*2)), fixc=(False, False), locn=(8, 9))
nodes[5] = GMTrussNode(xxyy=(leng*2*cos(pi/4*2), leng*2*sin(pi/4*2)), fixc=(False, False), locn=(10, 11))
nodes[6] = GMTrussNode(xxyy=(leng*1*cos(pi/4*3), leng*1*sin(pi/4*3)), fixc=(False, False), locn=(12, 13))
nodes[7] = GMTrussNode(xxyy=(leng*2*cos(pi/4*3), leng*2*sin(pi/4*3)), fixc=(False, False), locn=(14, 15))
nodes[8] = GMTrussNode(xxyy=(leng*1*cos(pi/4*4), leng*1*sin(pi/4*4)), fixc=(True, True), locn=(16, 17))
nodes[9] = GMTrussNode(xxyy=(leng*2*cos(pi/4*4), leng*2*sin(pi/4*4)), fixc=(True, True), locn=(18, 19))
nodes[5]._exfc.set_vector(xxyy=(exfc,0))  # external force

## --- section_mb: (GMTrussStructure) setting list of members --- ##
membs = list(range(19))  # list of truss members
area, yong = 10., 205.  # (cm^2), (kN/mm^2)
membs[0] = GMTrussMember(nodea=nodes[0], nodeb=nodes[2], area=area, yong=yong)
membs[1] = GMTrussMember(nodea=nodes[1], nodeb=nodes[3], area=area, yong=yong)
membs[2] = GMTrussMember(nodea=nodes[0], nodeb=nodes[3], area=area, yong=yong)
membs[3] = GMTrussMember(nodea=nodes[1], nodeb=nodes[2], area=area, yong=yong)
membs[4] = GMTrussMember(nodea=nodes[2], nodeb=nodes[3], area=area, yong=yong)

membs[5] = GMTrussMember(nodea=nodes[2], nodeb=nodes[4], area=area, yong=yong)
membs[6] = GMTrussMember(nodea=nodes[3], nodeb=nodes[5], area=area, yong=yong)
membs[7] = GMTrussMember(nodea=nodes[2], nodeb=nodes[5], area=area, yong=yong)
membs[8] = GMTrussMember(nodea=nodes[3], nodeb=nodes[4], area=area, yong=yong)
membs[9] = GMTrussMember(nodea=nodes[4], nodeb=nodes[5], area=area, yong=yong)

membs[10] = GMTrussMember(nodea=nodes[4], nodeb=nodes[6], area=area, yong=yong)
membs[11] = GMTrussMember(nodea=nodes[5], nodeb=nodes[7], area=area, yong=yong)
membs[12] = GMTrussMember(nodea=nodes[4], nodeb=nodes[7], area=area, yong=yong)
membs[13] = GMTrussMember(nodea=nodes[5], nodeb=nodes[6], area=area, yong=yong)
membs[14] = GMTrussMember(nodea=nodes[6], nodeb=nodes[7], area=area, yong=yong)

membs[15] = GMTrussMember(nodea=nodes[6], nodeb=nodes[8], area=area, yong=yong)
membs[16] = GMTrussMember(nodea=nodes[7], nodeb=nodes[9], area=area, yong=yong)
membs[17] = GMTrussMember(nodea=nodes[6], nodeb=nodes[9], area=area, yong=yong)
membs[18] = GMTrussMember(nodea=nodes[7], nodeb=nodes[8], area=area, yong=yong)


## --- section_mc: (GMTrussStructure) creating instance of structure --- ##")
strc = GMTrussStructure(nodes=nodes, membs=membs)

## --- section_md: (GMTrussStructure) building and solving matrix equation --- ##
strc.buld_matrixeq()
strc.solv_matrixeq()
strc.printclass('strc -> ')

## --- section_me: (GMTrussStructureAdvanced) drawing figure --- ##
strc.graph(
    scl_dfm=0.05/1, scl_frc=0.005/1,
    xlim=(-1-2,1+2), ylim=(-1-1, 1+3), fname='_b1' )

# =========================================================
# terminal log / terminal log / terminal log /
'''
'''
