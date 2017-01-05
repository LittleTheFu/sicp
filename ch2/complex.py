from math import atan2, sin, cos, pi
from fractions import gcd

# ---------------------------------------------------


def add_complex(z1, z2):
    return ComplexRI(z1.real + z2.real, z1.image + z2.image)


def mul_complex(z1, z2):
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)


class ComplexMA(object):

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def image(self):
        return self.magnitude * sin(self.angle)

    def __add__(self, other):
        return add_complex(self, other)

    def __mul__(self, other):
        return mul_complex(self, other)

    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)


class ComplexRI(object):

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        return add_complex(self, other)

    def __mul__(self, other):
        return mul_complex(self, other)

    @property
    def magnitude(self):
        return (self.real ** 2 + self.image ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.image, self.real)

    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.image)
# ---------------------------------------------------


class Rational(object):

    def __init__(self, number, denom):
        g = gcd(number, denom)
        self.number = number
        self.denom = denom

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.number, self.denom)


def add_rational(x, y):
    nx, dx = x.number, x.denom
    ny, dy = y.number, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    return Rational(x.number * y.number, x.denom * y.denom)


def iscomplex(z):
    return type(z) in (ComplexRI, ComplexMA)


def isrational(z):
    return type(z) == Rational

# ---------------------------------------------------


def add_complex_and_rational(z, r):
    return ComplexRI(z.real + r.number / r.denom, z.image)


def add_mix(z1, z2):
    if iscomplex(z1) and iscomplex(z2):
        return add_complex(z1, z2)
    elif iscomplex(z1) and isrational(z2):
        return add_complex_and_rational(z1, z2)
    elif isrational(z1) and iscomplex(z2):
        return add_complex_and_rational(z2, z1)
    else:
        return add_rational(z1, z2)
# ---------------------------------------------------


def add(z1, z2):
    types = (type_tag(z1), type_tag(z2))
    return add.imp[types](z1, z2)

add.imp = {}
add.imp[('com', 'com')] = add_complex
add.imp[('com', 'rat')] = add_complex_and_rational
add.imp[('rat', 'com')] = lambda x, y: add_complex_and_rational(y, x)
add.imp[('rat', 'rat')] = add_rational


def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat'}

# ---------------------------------------------------


def ration_to_complex(x):
    return ComplexRI(x.number / x.denom, 0)

coercions = {('rat', 'com'): ration_to_complex}


def coerce_add(x, y):
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if(tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif(ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercions possible'
    key = tx
    return coerce_add.imp[key](x, y)

coerce_add.imp = {'com': add_complex, 'rat': add_rational}
# ---------------------------------------------------


def main():
    print(add_complex(ComplexRI(1, 2), ComplexMA(2, pi / 2)))
    print(ComplexRI(1, 2) + ComplexMA(2, pi / 2))

    print(mul_complex(ComplexRI(0, 1), ComplexRI(0, 1)))
    print(ComplexRI(0, 1) * ComplexRI(0, 1))

    print('--------------------------------------------')

    c1 = ComplexRI(1, 2)
    c2 = ComplexRI(2, 2)
    r1 = Rational(1, 3)
    r2 = Rational(2, 5)

    print(add_mix(c1, c2))
    print(add_mix(c1, r1))
    print(add_mix(r1, c1))
    print(add_mix(r1, r2))
    print('===')

    print(add(c1, c2))
    print(add(c1, r1))
    print(add(r1, c1))
    print(add(r1, r2))
    print('===')

    print(coerce_add(c1, c2))
    print(coerce_add(c1, r1))
    print(coerce_add(r1, c1))
    print(coerce_add(r1, r2))
    print('--------------------------------------------')

if __name__ == "__main__":
    main()
