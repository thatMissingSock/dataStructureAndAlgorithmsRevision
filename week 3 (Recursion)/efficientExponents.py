def rec_pow(x, n):
    """
    This is an interesting one. And, I think, quite hard! We have to make a function for finding out the power of a number
    and we can do it recursively by going through each number, but he (Faris) proposes another quicker method.
    IF IT IS AN EVEN POWER, then we calculate half of the power recursively then multiply the number by itself.
    (x^(n/2) * x^(n/2)).
    IF IT IS AN ODD POWER, we subtract 1 from the power and do the above and then multiply that number by the original value
    of x.
    (x^(n/2) * x^(n/2)) * x.
    IF THE POWER IS 0, then we just return 1 because any number to the power of 0 is 1!
    :param x: A number.
    :param n: An integer representing the power.
    :return: The sum of that power.
    """
    # ~~~~PUT THE FOLLOWING CODE INTO PYTHONTUTOR AND MAKE EVERY TEST CASE EXCEPT FOR ONE A COMMENT TO SEE IT PROPERLY~~~~

    # I added some more comments because this one took a lil while
    # this is the first base case, if the power is 0 then we just return 1
    if n == 0:
        return 1

    # this is the second base case, in case the power is now even then we do the block of code
    if n % 2 == 0:
        # we force the recursion but instead of giving back the same value for n we floor divide it by 2 (floor divide
        # just means to divide and then round down)
        forcedRecursion = rec_pow(x, (n // 2))
        # the value of "forcedRecursion" should now be x^n/2 (after unwinding) and thus we just multiply these two values
        # by each other
        return (forcedRecursion * forcedRecursion)
    # this is the third base case, in case the power is now odd we do the following block of code
    elif n % 2 != 0:
        # we force the recursion, but instead of giving the same value for n we subtract 1 then floor divide by 2
        forcedRecursion = rec_pow(x, ((n - 1) // 2))
        # we then return the value of "forcedRecursion" multiplied by "forcedRecursion" and then AFTER multiply it again
        # by the value of x to make up for us subtracting 1 earlier
        return ((forcedRecursion * forcedRecursion) * x)


# test code provided by GPT
# Test cases for rec_pow(x, n)

# Base case: x^0 = 1
x, n = 2, 0
print(f"{rec_pow(x, n)} should be 1")  # Expected output: 1

# Power of 1: x^1 = x
x, n = 3, 1
print(f"{rec_pow(x, n)} should be 3")  # Expected output: 3

# Even power: x^2
x, n = 2, 2
print(f"{rec_pow(x, n)} should be 4")  # Expected output: 4

# Odd power: x^3
x, n = 2, 3
print(f"{rec_pow(x, n)} should be 8")  # Expected output: 8

# Larger even power
x, n = 5, 4
print(f"{rec_pow(x, n)} should be 625")  # Expected output: 625

# Larger odd power
x, n = 3, 5
print(f"{rec_pow(x, n)} should be 243")  # Expected output: 243

# Large power
x, n = 2, 10
print(f"{rec_pow(x, n)} should be 1024")  # Expected output: 1024

# Fractional base
x, n = 0.5, 3
print(f"{rec_pow(x, n)} should be 0.125")  # Expected output: 0.125

# Negative base with even power
x, n = -3, 4
print(f"{rec_pow(x, n)} should be 81")  # Expected output: 81

# Negative base with odd power
x, n = -2, 3
print(f"{rec_pow(x, n)} should be -8")  # Expected output: -8

# Zero base (non-zero exponent)
x, n = 0, 5
print(f"{rec_pow(x, n)} should be 0")  # Expected output: 0

# Edge case: Zero base with zero exponent (undefined, usually returns 1)
x, n = 0, 0
print(f"{rec_pow(x, n)} should be 1")  # Expected output: 1
