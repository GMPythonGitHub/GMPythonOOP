# gm_class_b_triangle.py: coded by Kinya MIURA 231126
# ---------------------------------------------------------
print('*** introducing class and function ***')
print('   *** triangle ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
import numpy as np

# ========================================================
## --- main process --- ##
pntax,pntay = 0,0; print(f'{(pntax,pntay) = }, ', end='')  # setting apexes
pntbx,pntby = 4,3; print(f'{(pntbx,pntby) = }, ', end='')
pntcx,pntcy = -3,4; print(f'{(pntcx,pntcy) = }')
# (pntax,pntay) = (0, 0), (pntbx,pntby) = (4, 3), (pntcx,pntcy) = (-3, 4)

sidea = np.sqrt((pntcx-pntbx)**2 + (pntcy-pntby)**2)  # calculating sides
sideb = np.sqrt((pntax-pntcx)**2 + (pntay-pntcy)**2)
sidec = np.sqrt((pntbx-pntax)**2 + (pntby-pntay)**2)
print(f'sidea = {sidea:g}, sideb = {sideb:g}, sidec = {sidec:g}')
# sidea = 7.07107, sideb = 5, sidec = 5

sss = (sidea+sideb+sidec) / 2  # calculating area
area = np.sqrt((sss-sidea) * (sss-sideb) * (sss-sidec) * sss)
print(f'{area = }')
# area = 12.5