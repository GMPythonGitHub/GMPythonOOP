# gm_coord_point_2d_func.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point movement in 2d with function ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (cos, sin, rad2deg as r2d, deg2rad as d2r)

# =========================================================
## --- function --- ##
def shift(xx, yy, ssx, ssy):  # shifting point
    xx += ssx; yy += ssy
    print(f'ssx = {ssx:g}, ssy = {ssy:g} >> xx = {xx:g}, yy = {yy:g}')
    return xx, yy
def scale(xx, yy, ccx, ccy) -> tuple:  # scaling point
    xx *= ccx; yy *= ccy
    print(f'ccx = {ccx:g}, ccy = {ccy:g} >> xx = {xx:g}, yy = {yy:g}')
    return xx, yy
def revolve(xx, yy, ps) -> tuple:  # revolving point
    xx, yy = xx * cos(ps) - yy * sin(ps), xx * sin(ps) + yy * cos(ps)
    print(f'ps = {r2d(ps):g} >> xx = {xx:g}, yy = {yy:g}')
    return xx, yy

# =========================================================
## --- main process --- ##
xx, yy = 3, 4  # setting point
print(f'xx = {xx:g}, yy = {yy:g}')
# xx = 3, yy = 4
xx, yy = shift(xx, yy, ssx=2, ssy=1)  # shifting point
# ssx = 2, ssy = 1 >> xx = 5, yy = 5
xx, yy = scale(xx, yy, ccx=2, ccy=3)  # scaling point
# ccx = 2, ccy = 3 >> xx = 10, yy = 15
xx, yy = revolve(xx, yy, ps=d2r(90))  # revolving point
# ps = 90 >> xx = -15, yy = 10
