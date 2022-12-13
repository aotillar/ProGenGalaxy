import math

def s_gravitational_parameter(m1,m2=0):
    """
    Takes two masses and calculates the standard graviational parameter bewtween
    the two of them. Often if one mass is signifigantly larger than the other one
    like with the sun and a planet, then the the smaller of the two masses is
    ommitted because it has a negliable effect.

    This was compared with the table found here
    https://en.wikipedia.org/wiki/Standard_gravitational_parameter
    and found to be correct.

    G is in Meter, kilogram, seconds
    
    """
    G = 6.674e-11
    if m2:
        m3 = m1 + m2
        return G * m3
    else:
        return G * m1


def orbital_period(a, m1, m2=0):
    """
    a = planet semi major axis in meters
    denom = standard gravitational parameter

    units need to be in meter, kg, seconds

    Ensure that Semi major axis data is given in meters, not km
    Typically orbits are in x*10^6 but they should be x*10^9
    """

    #return math.sqrt((4*math.pi**2/s_gravitational_parameter(m1,m2))*a**3)
    z = math.sqrt((4*math.pi**2/s_gravitational_parameter(m1,m2))*a**3)
    y = z/60
    x = y/60
    t = x/24
    return t

    

print(orbital_period(227.9e9,1.9891e30))
print(orbital_period(778.5e9,1.9891e30))
print(orbital_period(1432.0e9+120536,1.9891e30))
