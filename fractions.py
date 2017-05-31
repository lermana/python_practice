import operator



def _gcd(m, n):
    """recursively calculate and then return GCD of the 2 
    provided numbers. not the most efficient, and not 
    robust in the slightest, but nice & simple."""
    def recurse(m, n):
        if m % n == 0:
            return n
        else:
            return recurse(n, m % n)
    return recurse(m, n)


def _fraction_arithmetic(operation):
    """wrapper for arithmetic operations that catches TypeErrors."""
    def handle_value_errors(fraction, other):
        if not (isinstance(other, Fraction) or isinstance(other, int)):
            raise TypeError('Must pass Fractions or Fraction & int')
        else:
            return operation(fraction, other)
    return handle_value_errors


def _scaled_numerators(fraction_a, fraction_b):
    """allows for easily summing or comparing the numerators
    of 2 Fraction objects."""
    return (fraction_a.numerator * fraction_b.denominator,
            fraction_b.numerator * fraction_a.denominator)


def _add_fractions(fraction_a, fraction_b):
    """returns new Fraction that is the sum of the 2 passed
    Fraction objects.""" 
    return Fraction(sum(_scaled_numerators(fraction_a, fraction_b)),
                    fraction_a.denominator * fraction_b.denominator)


def _add_fraction_int(fraction, other):
    """returns sum of Fraction object & int, as new Fraction."""
    return Fraction(fraction.numerator + other * fraction.denominator,
                    fraction.denominator)


@_fraction_arithmetic
def _fraction_addition(fraction, other):
    """provids handling of TypeErrors, as well as both Fraction
    to Fraction and Fraction to int addition."""
    if isinstance(other, Fraction):
        return _add_fractions(fraction, other)
    else:
        return _add_fraction_int(fraction, other)


def _multiply_fractions(fraction_a, fraction_b):
    """returns new Fraction that is the product of the 2 passed
    Fraction objects.""" 
    return Fraction(fraction_a.numerator * fraction_b.numerator, 
                    fraction_a.denominator * fraction_b.denominator)


def _multiply_fraction_int(fraction, other):
    """returns product of Fraction object & int, as new Fraction."""
    return Fraction(fraction.numerator * other,
                    fraction.denominator)


@_fraction_arithmetic
def _fraction_multiplication(fraction, other):
    """provids handling of TypeErrors, as well as both Fraction
    to Fraction and Fraction to int multiplication."""
    if isinstance(other, Fraction):
        return _multiply_fractions(fraction, other)
    else:
        return _multiply_fraction_int(fraction, other)


def _divide_fractions(fraction_a, fraction_b):
    """returns quotient of 2 passed Fraction objects."""
    return _multiply_fractions(fraction_a, fraction_b._invert())


def _divide_fraction_int(fraction, other):
    """returns Fraction scaled downwards by passed int."""
    return Fraction(fraction.numerator, fraction.denominator * other)


@_fraction_arithmetic
def _fraction_division(fraction, other):
    """provids handling of TypeErrors, as well as both Fraction
    to Fraction and Fraction to int division."""
    if isinstance(other, Fraction):
        return _divide_fractions(fraction, other)
    else:
        return _divide_fraction_int(fraction, other)


def _compare_fractions(op_func):
    """wrapper for comparison operators. does not protect against
    issues arising from comparing a Fraction to a non-numeric type."""
    def operate(self, other):
        if isinstance(other, Fraction):
            return op_func(*_scaled_numerators(self, other))
        else:
            return op_func(self._real(), other)
    return operate



class Fraction:   
    """constructor takes numerator and denominator as arguments and retains 
    those values in lowest terms.
    
    constructor is robust with respect to handling of TypeErrors and 
    ZeroDivisionErrors. If a whole number is passed to constructor, a Fraction 
    object will not be created and instead the corresponding integer will be 
    returned. Only integers can be passed to the constructor; it cannot handle
    being passed Fraction objects, nor can it translate rational floating point
    numbers to fractions.

    the following arithmetic operations have been implmented for use with either
    other Fraction objects or integers:
        addition
        subtraction
        multiplication
        division

    and the following comparison operations have been implemented for use with
    other Fraction objects, integers, and floating point numbers (these 
    implementations may still run with other data types, which may or may
    not cause you problems):
        less than
        less than or equal to
        equal to
        not equal to
        greater than
        greater than or equal to

    the _real() and _invert() methods return, respectively, the real number representation
    and multiplicative inverse of the Fraction object."""

    def __new__(cls, numerator, denominator):
        if not (isinstance(numerator, int) 
                    and isinstance(denominator, int)):
            raise TypeError('Fraction constructors must both be integers')
        if denominator == 0:
            raise ZeroDivisionError('Fraction denominator must be non-zero int')
        
        if numerator == 0:
            return 0
        elif numerator % denominator == 0:
            return numerator // denominator
        else:
            return super(Fraction, cls).__new__(cls)

    def __init__(self, numerator, denominator):
        if not (isinstance(numerator, int) 
                    and isinstance(denominator, int)):
            raise TypeError('Fraction constructors must both be integers')
        if denominator == 0:
            raise ZeroDivisionError('Fraction denominator must be non-zero int')

        if denominator < 0 and numerator >= 0:
            numerator, denominator = -1 * numerator, -1 * denominator
        common = _gcd(numerator, denominator)

        self.numerator = numerator // common
        self.denominator = denominator // common

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)
    
    def __repr__(self):
        return self.__str__()

    def __neg__(self):
        return self.__mul__(-1)

    def _real(self):
        return self.numerator / self.denominator

    def _invert(self):
        return Fraction(self.denominator, self.numerator)

    def __add__(self, other):
        return _fraction_addition(self, other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other.__neg__())   

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        return _fraction_multiplication(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return _fraction_division(self, other)

    def __rtruediv__(self, other):
        return self._invert().__mul__(other)

    @_compare_fractions
    def __lt__(self, other):
         return operator.lt(self, other)

    @_compare_fractions
    def __le__(self, other):
        return operator.le(self, other)
    
    @_compare_fractions
    def __eq__(self, other):
        return operator.eq(self, other)

    @_compare_fractions
    def __ne__(self, other):
        return operator.ne(self, other)

    @_compare_fractions
    def __gt__(self, other):
        return operator.gt(self, other)

    @_compare_fractions
    def __ge__(self, other):
        return operator.ge(self, other)
