# gm_class_numbers_a.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMNumbersA: operating numbers ***')
print('   *** minimum version ***')

# =========================================================
print('### --- section_class: (GMNumbersA) declaring class --- ###')
class GMNumbersA():
    ## --- section_a: initializing class instance --- ##
    def __init__(self) -> None:
        self.aa, self.bb = None, None  # instance variables

# =========================================================
print('### --- section_main: (GMMumbersA) main process --- ###')
## --- section_m0: calculating arithmetics --- ##
numbs = GMNumbersA()  # creating instance with default values
numbs.aa, numbs.bb = 3, 2
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = (  # using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }')
# ---------------------------------------------------------
numbs.aa, numbs.bb = 7, 3  # setting instance valuables
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = (  # using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }\n')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbers1 for operating numbers ***
   *** minimum version ***
### --- section_class: (GMNumbersA) declaring class --- ###
### --- section_main: (GMMumbersA) main process --- ###
numbs.aa = 3, numbs.bb = 2
add = 5, sub = 1
numbs.aa = 7, numbs.bb = 3
add = 10, sub = 4
'''
