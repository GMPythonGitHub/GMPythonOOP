# gm_coord_point_2d.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point movement in 2d ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (cos, sin, rad2deg as r2d, deg2rad as d2r)

# =========================================================
## --- main process --- ##
xx, yy = 3, 4  # setting point
print(f'xx = {xx:g}, yy = {yy:g}')
# xx = 3, yy = 4

ssx, ssy = 2, 1  # shifting point
xx += ssx; yy += ssy
print(f'ssx = {ssx:g}, ssy = {ssy:g} >> xx = {xx:g}, yy = {yy:g}')
# ssx = 2, ssy = 1 >> xx = 5, yy = 5

ccx, ccy = 2, 3  # scaling point
xx *= ccx; yy *= ccy
print(f'ccx = {ccx:g}, ccy = {ccy:g} >> xx = {xx:g}, yy = {yy:g}')
# ccx = 2, ccy = 3 >> xx = 10, yy = 15

ps = d2r(90)  # revolving point
xx, yy = xx * cos(ps) - yy * sin(ps), xx * sin(ps) + yy * cos(ps)
print(f'ps = {r2d(ps):g} >> xx = {xx:g}, yy = {yy:g}' )
# ps = 90 >> xx = -15, yy = 10
