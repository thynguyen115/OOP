""" Maths in complex numbers """
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return str(Complex(self.real + no.real, self.imaginary + no.imaginary))
        
    def __sub__(self, no):
        return str(Complex(self.real - no.real, self.imaginary - no.imaginary))        
    
    def __mul__(self, no):
        """x = a + bi; y = c + di
        x*y = (a+bi)(c+di) = ac + adi + bci - bd = (ac-bd) + (ad+bc)i
        """
        return str(Complex(self.real * no.real - self.imaginary*no.imaginary,
        self.real*no.imaginary + self.imaginary*no.real))
    
    def __truediv__(self, no):
        """x/y = (a+bi)/(c+di)=(a+bi)(c-di)/(c+di)(c-di)
        (ac - adi + bci + bd) / (c^2 + d^2)
        = ((ac+bd)+(bc-ad)i) / (c^2 + d^2)
        """
        denominator = no.real**2 + no.imaginary**2
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_part = (a*c + b*d)/denominator
        imaginary_part = (b*c - a*d)/denominator
        return str(Complex(real_part, imaginary_part))
    
    def mod(self):
        """ mod(a+bi) = sqrt(a^2 + b^2) """
        return str(Complex((self.real**2 + self.imaginary**2)**(1/2),0))
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
