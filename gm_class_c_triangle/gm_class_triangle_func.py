# gm_class_triangle_func.py: coded by Kinya MIURA 231126
# ---------------------------------------------------------
print('*** introducing class and function ***')
print('   *** triangle: with function ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
import numpy as np

# ========================================================
## --- function --- ##
def dst(ppa, ppb):  # calculating distance between points
    return np.sqrt((ppb[0]-ppa[0])**2 + (ppb[1]-ppa[1])**2)

def ara(ssa, ssb, ssc):  # calculating area
    sss = (ssa+ssb+ssc) / 2
    return np.sqrt((sss-ssa) * (sss-ssb) * (sss-ssc) * sss)

# ========================================================
## --- main process --- ##
pntax,pntay = 0,0; print(f'{(pntax,pntay) = }, ', end='')  # setting apexes
pntbx,pntby = 4,3; print(f'{(pntbx,pntby) = }, ', end='')
pntcx,pntcy = -3,4; print(f'{(pntcx,pntcy) = }')
# (pntax,pntay) = (0, 0), (pntbx,pntby) = (4, 3), (pntcx,pntcy) = (-3, 4)

sidea = dst((pntcx,pntcy), (pntbx,pntby))  # calculating sides
sideb = dst((pntax,pntay), (pntcx,pntcy))
sidec = dst((pntbx,pntby), (pntax,pntay))
print(f'sidea = {sidea:g}, sideb = {sideb:g}, sidec = {sidec:g}')
# sidea = 7.07107, sideb = 5, sidec = 5

area = ara(sidea, sideb, sidec)  # calculating area
print(f'{area = }')
# area = 12.5