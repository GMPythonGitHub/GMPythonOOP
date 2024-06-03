# gm_cta06_OOP_truss_adv_prob_a2.py: coded by Kinya MIURA 240530
# ---------------------------------------------------------
print("\n*** (GMTrussStructure) class for segment ***")
print("  *** class GMTrussNode, GMTrussMemberAdvanced are embedded as nodes and membs ***")
# ---------------------------------------------------------
print("### --- section_module: (GMTrussStructure) importing items from module --- ###")
from gm_cta06_OOP_truss_adv2_structure import (
    GMTrussNode, GMTrussMember, GMTrussStructure )

# =========================================================

print("### --- section_main: (GMTrussStructure) setting structure --- ###")

nstry = 2  # number of stories

## --- section_ma: (GMTrussStructure) setting list of nodes --- ##
nodes = []  # empty list of truss nodes
leng, exfc = 1., 100.  # (m), (kN)
for inode in range(2 + 2 * nstry):
    istry = inode // 2  # story number
    icolm = inode % 2  # column number
    nodes.append(GMTrussNode(xxyy=(leng * icolm, leng * istry), locn=(inode * 2 + 0, inode * 2 + 1)))
    if istry == 0:  # nodes on the ground
        nodes[-1].set_truss_node(fixc=(True, True))
    else:
        nodes[-1].set_truss_node(fixc=(False, False))
nodes[nstry*2]._exfc.set_vector(xxyy=(exfc, 0.))  # external force

## --- section_mb: (GMTrussStructure) setting list of members --- ##
membs = []  # empty list of truss members
area, yong = 10., 205.  # (cm^2), (kN/mm^2)
for imemb in range(5 * nstry):  # n-story membs
    istry = imemb // 5  # story number
    icolm = imemb % 5  # column
    nodeo = istry * 2  # initial node number
    membs.append(GMTrussMember(nodea=None, nodeb=None, area=area, yong=yong))
    if icolm == 0:
        membs[-1]._nodea, membs[-1]._nodeb = nodes[nodeo+0], nodes[nodeo+2]
    elif icolm == 1:
        membs[-1]._nodea, membs[-1]._nodeb = nodes[nodeo+1], nodes[nodeo+3]
    elif icolm == 2:
        membs[-1]._nodea, membs[-1]._nodeb = nodes[nodeo+2], nodes[nodeo+3]
    elif icolm == 3:
        membs[-1]._nodea, membs[-1]._nodeb = nodes[nodeo+0], nodes[nodeo+3]
    elif icolm == 4:
        membs[-1]._nodea, membs[-1]._nodeb = nodes[nodeo+1], nodes[nodeo+2]

## --- section_mc: (GMTrussStructure) creating instance of structure --- ##")
strc = GMTrussStructure(nodes=nodes, membs=membs)

## --- section_md: (GMTrussStructure) building and solving matrix equation --- ##
strc.buld_matrixeq()
strc.solv_matrixeq()
strc.printclass('strc -> ')

## --- section_me: (GMTrussStructureAdvanced) drawing figure --- ##
strc.graph(
    scl_dfm=0.05/nstry, scl_frc=0.005/nstry,
    xlim=(-1.0,1+nstry), ylim=(-1.0, 1+nstry), fname='_a2' )

# =========================================================
# terminal log / terminal log / terminal log /
'''
'''
