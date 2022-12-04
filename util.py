from sage.misc.functional import n
from sage.symbolic.constants import pi
from sage.misc.decorators import infix_operator

def fmt(v):
    return f'{n(v):0,.2f}'

def printnum(v):
    print(fmt(v))
    
def radians(degrees):
    return degrees * pi/180

def degrees(radians):
    return radians * 180/pi

@infix_operator('or')
def pipe(a, b):
    return b(a)