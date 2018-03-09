"""
Skrypt Cantera
"""
from Cantera import *

X = 'H2:2 O2:1 N2:3.76'
P = 101325
T = 300
gast.TPX = T, P, X
print(gas)
