# gm_cta06_OOP_truss_adv_prob_a1.py: coded by Kinya MIURA 240530
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
if nstry == 1:
    nodes[0] = GMTrussNode(
        xxyy=(leng*0, leng*0), fixc=(True, True), locn=(0, 1) )
    nodes[1] = GMTrussNode(
        xxyy=(leng*1, leng*0), fixc=(True, True), locn=(2, 3) )
    nodes[2] = GMTrussNode(
        xxyy=(leng*0, leng*1), fixc=(False, False), locn=(4, 5) )
    nodes[2]._exfc.set_vector(xxyy=(exfc, 0.))
    nodes[3] = GMTrussNode(
        xxyy=(leng*1, leng*1), fixc=(False, False), locn=(6, 7) )
if nstry == 2:
    nodes[0] = GMTrussNode(
        xxyy=(leng*0, leng*0), fixc=(True, True), locn=(0, 1) )
    nodes[1] = GMTrussNode(
        xxyy=(leng*1, leng*0), fixc=(True, True), locn=(2, 3) )
    nodes[2] = GMTrussNode(
        xxyy=(leng*0, leng*1), fixc=(False, False), locn=(4, 5) )
    nodes[3] = GMTrussNode(
        xxyy=(leng*1, leng*1), fixc=(False, False), locn=(6, 7) )
    nodes[4] = GMTrussNode(
        xxyy=(leng*0, leng*2), fixc=(False, False), locn=(8, 9) )
    nodes[4]._exfc.set_vector(xxyy=(exfc, 0.))
    nodes[5] = GMTrussNode(
        xxyy=(leng*1, leng*2), fixc=(False, False), locn=(10, 11) )

## --- section_mb: (GMTrussStructure) setting list of members --- ##
membs = list(range(5 * nstry))  # list of truss members
area, yong = 10., 205.  # (cm^2), (kN/mm^2
if nstry == 1:
    membs[0] = GMTrussMember(
        nodea=nodes[0], nodeb=nodes[2], area=area, yong=yong)
    membs[1] = GMTrussMember(
        nodea=nodes[1], nodeb=nodes[3], area=area, yong=yong)
    membs[2] = GMTrussMember(
        nodea=nodes[2], nodeb=nodes[3], area=area, yong=yong)
    membs[3] = GMTrussMember(
        nodea=nodes[0], nodeb=nodes[3], area=area, yong=yong)
    membs[4] = GMTrussMember(
        nodea=nodes[1], nodeb=nodes[2], area=area, yong=yong)
if nstry == 2:
    membs[0] = GMTrussMember(
        nodea=nodes[0], nodeb=nodes[2], area=area, yong=yong)
    membs[1] = GMTrussMember(
        nodea=nodes[1], nodeb=nodes[3], area=area, yong=yong)
    membs[2] = GMTrussMember(
        nodea=nodes[2], nodeb=nodes[3], area=area, yong=yong)
    membs[3] = GMTrussMember(
        nodea=nodes[0], nodeb=nodes[3], area=area, yong=yong)
    membs[4] = GMTrussMember(
        nodea=nodes[1], nodeb=nodes[2], area=area, yong=yong)
    membs[5] = GMTrussMember(
        nodea=nodes[2], nodeb=nodes[4], area=area, yong=yong)
    membs[6] = GMTrussMember(
        nodea=nodes[3], nodeb=nodes[5], area=area, yong=yong)
    membs[7] = GMTrussMember(
        nodea=nodes[4], nodeb=nodes[5], area=area, yong=yong)
    membs[8] = GMTrussMember(
        nodea=nodes[2], nodeb=nodes[5], area=area, yong=yong)
    membs[9] = GMTrussMember(
        nodea=nodes[3], nodeb=nodes[4], area=area, yong=yong)

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

# =========================================================
# terminal log / terminal log / terminal log /
'''
'''
