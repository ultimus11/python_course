def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a // b

def absolute(a):
    return abs(a)

def maximum(a, b):
    return max(a, b)

def minimum(a, b):
    return min(a, b)

def sin(a):
    #without math take sin of a
    return a

def factorial(n):
    """Calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sine(x, terms=10):
    """
    Calculate sine of x using the Taylor series expansion.
    x: The input angle in radians.
    terms: The number of terms in the Taylor series to compute.
    """
    sine_value = 0
    for i in range(terms):
        # Alternating signs for the series: (-1)^i
        sign = (-1) ** i
        # Calculate the term: x^(2i+1) / (2i+1)!
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sine_value += sign * term
    return sine_value

def cosine(x, terms=10):
    """
    Calculate cosine of x using the Taylor series expansion.
    x: The input angle in radians.
    terms: The number of terms in the Taylor series to compute.
    """
    cosine_value = 0
    for i in range(terms):
        # Alternating signs for the series: (-1)^i
        sign = (-1) ** i
        # Calculate the term: x^(2i) / (2i)!
        term = (x ** (2 * i)) / factorial(2 * i)
        cosine_value += sign * term
    return cosine_value

def tangent(x, terms=10):
    """
    Calculate tangent of x using the Taylor series expansion.
    x: The input angle in radians.
    terms: The number of terms in the Taylor series to compute.
    """
    return sine(x, terms) / cosine(x, terms)

def arcsine(x, terms=10):
    """
    Calculate arcsine of x using the Taylor series expansion.
    x: The input value in the range [-1, 1].
    terms: The number of terms in the Taylor series to compute.
    """
    arcsine_value = 0
    for i in range(terms):
        # Calculate the term: (2i)! / (4^i * (i!)^2 * (2i+1)) * x^(2i+1)
        term = factorial(2 * i) / (4 ** i * (factorial(i) ** 2) * (2 * i + 1)) * (x ** (2 * i + 1))
        arcsine_value += term
    return arcsine_value

def arccosine(x, terms=10):
    """
    Calculate arccosine of x using the Taylor series expansion.
    x: The input value in the range [-1, 1].
    terms: The number of terms in the Taylor series to compute.
    """
    return (3.14 / 2) - arcsine(x, terms)

def arctangent(x, terms=10):
    """
    Calculate arctangent of x using the Taylor series expansion.
    x: The input value.
    terms: The number of terms in the Taylor series to compute.
    """
    arctangent_value = 0
    for i in range(terms):
        # Calculate the term: (-1)^i * x^(2i+1) / (2i+1)
        term = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        arctangent_value += term
    return arctangent_value

def natural_log(x, terms=10):
    """
    Calculate the natural logarithm of (1 + x) using the Taylor series expansion.
    x: the number (1 + x) for which we want to compute ln(1 + x)
    terms: the number of terms to use for the approximation
    """
    if x <= -1:
        raise ValueError("x must be greater than -1 for the series to converge.")
    
    result = 0
    for i in range(1, terms + 1):
        # Alternating series: (-1)^(i-1)
        term = ((-1)**(i-1)) * (x**i) / i
        result += term
    return result

def log_base(n, base=2, terms=10):
    """
    Calculate logarithm of n to a given base using the change of base formula:
    log_base(n) = ln(n) / ln(base)
    """
    if n <= 0:
        raise ValueError("n must be greater than 0.")
    if base <= 0:
        raise ValueError("Base must be greater than 0.")
    
    # Change of base formula: log_base(n) = ln(n) / ln(base)
    ln_n = natural_log(n - 1, terms)  # Using ln(n) = ln(1 + (n - 1))
    ln_base = natural_log(base - 1, terms)
    
    return ln_n / ln_base

def square_root(x, terms=10):
    """
    Calculate the square root of x using the Taylor series expansion.
    x: the number for which we want to compute the square root
    terms: the number of terms to use for the approximation
    """
    if x < 0:
        raise ValueError("x must be greater than or equal to 0.")
    
    result = 0
    for i in range(terms):
        # Calculate the term: (-1)^i * (2i-1)!! / (2i)!! * x^(i)
        term = ((-1) ** i) * factorial(2 * i - 1) / (factorial(2 * i) * (2 ** i)) * (x ** i)
        result += term
    return result

def cube_root(x, terms=10):
    """
    Calculate the cube root of x using the Taylor series expansion.
    x: the number for which we want to compute the cube root
    terms: the number of terms to use for the approximation
    """
    if x < 0:
        raise ValueError("x must be greater than or equal to 0.")
    
    result = 0
    for i in range(terms):
        # Calculate the term: (-1)^i * (3i-1)!! / (3i)!! * x^(i)
        term = ((-1) ** i) * factorial(3 * i - 1) / (factorial(3 * i) * (3 ** i)) * (x ** i)
        result += term
    return result

def exponential(x, terms=10):
    """
    Calculate the exponential function e^x using the Taylor series expansion.
    x: the exponent for the exponential function
    terms: the number of terms to use for the approximation
    """
    result = 0
    for i in range(terms):
        # Calculate the term: x^i / i!
        term = (x ** i) / factorial(i)
        result += term
    return result

def power_base(x, y, terms=10):
    """
    Calculate x raised to the power of y using the Taylor series expansion.
    x: the base
    y: the exponent
    terms: the number of terms to use for the approximation
    """
    result = 0
    for i in range(terms):
        # Calculate the term: y * (y-1) * ... * (y-i+1) * x^i / i!
        term = (y * (y - 1) * ... * (y - i + 1) * (x ** i)) / factorial(i)
        result += term
    return result

