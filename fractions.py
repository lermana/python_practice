import operator

def gcd(m, n):
    def recurse(m, n):
        if m % n == 0:
            return n
        else:
            return recurse(n, m % n)
    return recurse(m, n)


class Fraction:   
    
    def __new__(cls, numerator, denomenator):
        if numerator == 0:
            return 0
        else:
            return super(Fraction, cls).__new__(cls)

    def __init__(self, numerator, denomenator):
        if not (isinstance(numerator, int) 
                    and isinstance(denomenator, int)):
            raise ValueError('Fraction constructors must both be integers')
        
        if denomenator == 0:
            raise ValueError('Fraction denomenator must be non-zero int')

        if denomenator < 0 and numerator >= 0:
            numerator, denomenator = -1 * numerator, -1 * denomenator
        
        common = gcd(numerator, denomenator)
        self.numerator = numerator // common
        self.denomenator = denomenator // common

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denomenator)
    
    def __repr__(self):
        return self.__str__()

    def _real(self):
        return self.numerator / self.denomenator

    def _invert(self):
        return Fraction(self.denomenator, self.numerator)

    def __neg__(self):
        return self.__mul__(-1)

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denomenator 
                               + other.numerator * self.denomenator, 
                            self.denomenator * other.denomenator)
        elif isinstance(other, int):
            if other == 0:
                return self
            else:
                return self.__add__(Fraction(other, 1))
        else:
            raise ValueError('Must pass Fractions or Fraction & int')

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other.__neg__())   

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, 
                            self.denomenator * other.denomenator)    
        elif isinstance(other, int):
            if other == 0:
                return 0
            else:
                return self.__mul__(Fraction(other, 1))
        else:
            raise ValueError('Must pass Fractions or Fraction & int')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self.__mul__(other._invert())  
        elif isinstance(other, int):
            if other == 0:
                raise ValueError('Can\'t divide by zero')
            else:
                return self.__mul__(Fraction(1, other))
        else:
            raise ValueError('Must pass Fractions or Fraction & int')

    def __rtruediv__(self, other):
        return self._invert().__mul__(other)

    def _compare(op_func):
        def operate(self, other):
            if isinstance(other, Fraction):
                return op_func(self.numerator 
                                    * other.denomenator,
                                other.numerator 
                                    * self.denomenator)
            else:
                return op_func(self._real(), other)
        return operate

    @_compare
    def __lt__(self, other):
         return operator.lt(self, other)

    @_compare
    def __le__(self, other):
        return operator.le(self, other)
    
    @_compare
    def __eq__(self, other):
        return operator.eq(self, other)

    @_compare
    def __ne__(self, other):
        return operator.ne(self, other)

    @_compare
    def __gt__(self, other):
        return operator.gt(self, other)

    @_compare
    def __ge__(self, other):
        return operator.ge(self, other)
