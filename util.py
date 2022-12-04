import functools
from sage.misc.functional import n
from sage.symbolic.constants import pi
from sage.misc.decorators import infix_operator
from sage.functions.trig import sin, cos, tan


def fmt(v):
    return f'{n(v):0,.2f}'

def printv(*args):
  if len(args) == 1:
    print(fmt(args[0]))
  else:
    label, value = args
    print(f'{label} = {fmt(value)}')

def radians(degrees):
    return degrees * pi/180

def degrees(radians):
    return radians * 180/pi

@infix_operator('or')
def pipe(a, b):
    return b(a)

def use_degrees(f):
    """
    Wrap a one-argument function so that it converts the argument from degrees to radians before applying
    """
    @functools.wraps(f)
    def wrapped_function(v):
        return f(radians(v))

    return wrapped_function

sind = use_degrees(sin)
cosd = use_degrees(cos)
tand = use_degrees(tan)
