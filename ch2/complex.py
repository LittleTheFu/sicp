from math import atan2, sin, cos, pi


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


def main():
    print(add_complex(ComplexRI(1, 2), ComplexMA(2, pi / 2)))
    print(ComplexRI(1, 2) + ComplexMA(2, pi / 2))

    print(mul_complex(ComplexRI(0, 1), ComplexRI(0, 1)))
    print(ComplexRI(0, 1) * ComplexRI(0, 1))


if __name__ == "__main__":
    main()
