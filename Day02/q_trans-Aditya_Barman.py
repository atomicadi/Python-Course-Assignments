# written by Aditya Barman, Date: April. 24, 2026; @weizmann
# calculating translational partition function

import math
from scipy import constants

h = constants.h
k_B = constants.k

m = float(input("Please put the value of mass (in kg unit): "))
T = float(input("Please put the temperature (in K unit): "))
V = float(input("Please put the volume (in m3 unit), if there is no V, put 1: "))

q_trans = ((2*(math.pi)*m*k_B*T)/h**2)**(3/2) * V
print("The calculated value of translational partition function (using your input) is, ", q_trans)