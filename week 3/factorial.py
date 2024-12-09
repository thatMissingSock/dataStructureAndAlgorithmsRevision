def factorial(n):
    """
    Same restrictions as before. We need this function to do the factorial based on n (the number of times to do factorial).
    The meaning of factorial is the product of all the positive integers <= n. So 4 would be 4X3X2X1 = 24. Factorial of 0
    is counted as 1.
    :param n: An integer.
    :return: The factorial of n.
    """
    if n == 0:
        return 1

    return n * factorial(n - 1)

# test code provided by GPt
# Test cases for factorial(n)

# Base case: Factorial of 0
n = 0
print(f"{factorial(n)} should be 1")  # Expected output: 1

# Factorial of 1
n = 1
print(f"{factorial(n)} should be 1")  # Expected output: 1

# Factorial of 2
n = 2
print(f"{factorial(n)} should be 2")  # Expected output: 2

# Factorial of 3
n = 3
print(f"{factorial(n)} should be 6")  # Expected output: 6

# Factorial of 4
n = 4
print(f"{factorial(n)} should be 24")  # Expected output: 24

# Factorial of 5
n = 5
print(f"{factorial(n)} should be 120")  # Expected output: 120

# Factorial of 10
n = 10
print(f"{factorial(n)} should be 3628800")  # Expected output: 3628800

# Factorial of 20
n = 20
print(f"{factorial(n)} should be 2432902008176640000")  # Expected output: 2432902008176640000

# Large factorial
n = 50
expected = 1
for i in range(1, n + 1):
    expected *= i
print(f"{factorial(n)} should be {expected}")  # Expected output: 50 factorial

