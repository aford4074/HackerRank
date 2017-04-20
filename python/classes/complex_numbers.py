'''
Classes: Dealing with Complex Numbers
'''

from math import sqrt

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                        self.real * no.imaginary + self.imaginary * no.real)

    def __truediv__(self, no):
        conjugate = Complex(no.real, no.imaginary * -1)

        q = self * conjugate
        d = no * conjugate

        return Complex(q.real / d.real, q.imaginary / d.real)

    def mod(self):
        return Complex(sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        return '%.2f%c%.2fi' % (self.real, '+' if self.imaginary >= 0 else '-', abs(self.imaginary))

if __name__ == '__main__':
    c = [2, 1]
    d = [5, 6]
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
