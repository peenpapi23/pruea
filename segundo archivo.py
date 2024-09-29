import math

class Lb:
    def __init__(self):
        pass

    def sumaC(self, a, b):
        real = (a[0] + b[0])
        imag = (a[1] + b[1])
        return (real, imag)

    def multiC(self, a, b):
        real = (a[0] * b[0]) - (a[1] * b[1])
        imag = (a[0] * b[1]) + (a[1] * b[0])
        return (real, imag)

    def restaC(self, a, b):
        real = (a[0] - b[0])
        imag = (a[1] - b[1])
        return (real, imag)

    def divisionC(self, a, b):
        real = ((a[0] * b[0]) + (a[1] * b[1])) / ((b[0]**2) + (b[1]**2))
        imag = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0]**2) + (b[1]**2))
        return (real, imag)

    def moduloC(self, a):
        return ((a[0]**2) + (a[1]**2))**(1/2)

    def conjugadoC(self, a):
        imag = -1 * (a[1])
        return (a[0], imag)

    def faseC(self, a):
        fase = math.atan2(a[0], a[1])
        return fase

    def converC_P(self, a):
        modulo = self.moduloC(a)
        fase = self.faseC(a)
        return (modulo, fase)

    def converP_C(self, a):
        real = a[0] * math.cos(a[1])
        imag = a[0] * math.sin(a[1])
        return (real, imag)
