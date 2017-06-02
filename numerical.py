def newton_raphson(func, func_prime, guess, eps):
	while abs(func(guess)) >= eps:
		guess -= func(guess) / func_prime(guess, eps)
	return guess


def approx_deriv(func):
	def differentiate(x, eps):	
		h = x * eps
		return (func(x + h) 
					- func(x - h)
					) / (2 * h)
	return differentiate


def find_roots_univariate(func, eps):
	return newton_raphson(func, 
						  approx_deriv(func),
						  (func(0) / 2).__neg__(), 
						  eps)


def nth_root(n, num, eps=None):
	if eps is None: eps = num/10000
	return find_roots_univariate(lambda x: x ** n - num,
						  		 eps)


def sqrt(num, eps=None):
	return nth_root(2, num, eps)


def cubrt(num, eps=None):
	return nth_root(3, num, eps)