from math import pi, e
from math import sin, cos, tan, asin, acos, atan, sqrt, log, exp, pow, degrees, radians
e0 = 8.854187817e-12
mu0 = 4*pi*1e-7
h=6.62607004e-34 # m^2kg/s
na=6.0221415e23
cal2j = 4.184
j2cal = 1/4.184
c=299792458 # m/s
Rjoules = 8.31446261815324
Ratm = 0.082057366080960
Rtorr = 62.363598221529


biotsavart = 'B=(mu0*I)/(2*pi*R)'
faraday = 'emf induced in loop = - dphi/dt'
ampere = 'integral of B dot dl = mu0 * I enclosed'
magnetic_field_from_wire = 'B = bsk*I/R'

bsk = 2e-7

class Neutron:
    mass=1.67493e-27 # kg
class Electron:
    mass=9.10939e-31 # kg

def ln(x):
    return log(x)