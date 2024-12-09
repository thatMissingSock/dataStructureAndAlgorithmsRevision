def geomseries(x):
    """
    Given a list of numbers (x), we need to find the sum of the geometric series. This basically means that the values of
    the numbers in the list can be represented by algebra.
    Let us say x = [2, 12, 3, 4, 5] then this can be seen as [a, b, c, d, e].
    Then we can find out the sum of the equation, which would be (a + ab + abc + abcd + abcde).
    MATHEMATICALLY, this can be represented as a X (b + 1 X (c + 1 X (d + 1 X (e + 1)))) and it works. Why? Fuck knows
    but, I checked and it does indeed work ;~;.
    :param x: A list of numbers.
    :return: The total of x using a geometric formula.
    """

    if x == []:
        return 0

    head = x[0]
    tail = x[1:]

    return head * (geomseries(tail) + 1)



# test code provided by GPT
# Test cases for geomseries(x)

# Base case: Empty list
x = []
print(f"{geomseries(x)} should be 0")  # Expected output: 0

# Single-element list
x = [3]
print(f"{geomseries(x)} should be 3")  # Expected output: 3

# Two-element list
x = [2, 4]
# Calculation: 2 + (2 * 4) = 2 + 8 = 10
print(f"{geomseries(x)} should be 10")  # Expected output: 10

# Three-element list
x = [1, 2, 3]
# Calculation: 1 + (1 * 2) + (1 * 2 * 3) = 1 + 2 + 6 = 9
print(f"{geomseries(x)} should be 9")  # Expected output: 9

# Four-element list
x = [2, 3, 4, 5]
# Calculation: 2 + (2 * 3) + (2 * 3 * 4) + (2 * 3 * 4 * 5)
# = 2 + 6 + 24 + 120 = 152
print(f"{geomseries(x)} should be 152")  # Expected output: 152

# List with all ones
x = [1, 1, 1, 1]
# Calculation: 1 + 1 + 1 + 1 = 4
print(f"{geomseries(x)} should be 4")  # Expected output: 4

# List with zeros
x = [0, 2, 3]
# Calculation: 0 + (0 * 2) + (0 * 2 * 3) = 0
print(f"{geomseries(x)} should be 0")  # Expected output: 0

# List with negative numbers
x = [-2, 3, -4]
# Calculation: -2 + (-2 * 3) + (-2 * 3 * -4) = -2 - 6 + 24 = 16
print(f"{geomseries(x)} should be 16")  # Expected output: 16

# List with a mix of integers and floats
x = [1.5, 2, 2.5]
# Calculation: 1.5 + (1.5 * 2) + (1.5 * 2 * 2.5) = 1.5 + 3 + 7.5 = 12
print(f"{geomseries(x)} should be 12.0")  # Expected output: 12.0

# Larger list
x = [2, 2, 2, 2, 2]
# Calculation: 2 + (2 * 2) + (2 * 2 * 2) + (2 * 2 * 2 * 2) + (2 * 2 * 2 * 2 * 2)
# = 2 + 4 + 8 + 16 + 32 = 62
print(f"{geomseries(x)} should be 62")  # Expected output: 62

# ~~~~~~~~~~~~~~~~~~~~~He mentioned about doing it iteratively so I did that too :)~~~~~~~~~~~~~~~~~~~~~

def iterativeGeomSeries(x):
    """
    This is the same as before but done iteratively as the first equation:
    Let us say x = [2, 12, 3, 4, 5] then this can be seen as [a, b, c, d, e].
    Then we can find out the sum of the equation, which would be (a + ab + abc + abcd + abcde).
    :param x: A list.
    :return: The sum of x using the geometricSeries formula.
    """
    if x == []:
        return 0

    tempOutput = 0
    for i in range(len(x)):
        tempSum = x[i]
        if i > 0:
            for j in range(i):
                tempSum *= x[j]
        tempOutput += tempSum

    return tempOutput
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~THE FOLLOWING IS FOR THE ITERATIVE GEO SERIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# test code provided by me :)
# Test cases for iterativeGeomSeries(x)

# Base case: Empty list
x = []
print(f"{iterativeGeomSeries(x)} should be 0")  # Expected output: 0

# Single-element list
x = [3]
print(f"{iterativeGeomSeries(x)} should be 3")  # Expected output: 3

# Two-element list
x = [2, 4]
# Calculation: 2 + (2 * 4) = 2 + 8 = 10
print(f"{iterativeGeomSeries(x)} should be 10")  # Expected output: 10

# Three-element list
x = [1, 2, 3]
# Calculation: 1 + (1 * 2) + (1 * 2 * 3) = 1 + 2 + 6 = 9
print(f"{iterativeGeomSeries(x)} should be 9")  # Expected output: 9

# Four-element list
x = [2, 3, 4, 5]
# Calculation: 2 + (2 * 3) + (2 * 3 * 4) + (2 * 3 * 4 * 5)
# = 2 + 6 + 24 + 120 = 152
print(f"{geomseries(x)} should be 152")  # Expected output: 152

# List with all ones
x = [1, 1, 1, 1]
# Calculation: 1 + 1 + 1 + 1 = 4
print(f"{iterativeGeomSeries(x)} should be 4")  # Expected output: 4

# List with zeros
x = [0, 2, 3]
# Calculation: 0 + (0 * 2) + (0 * 2 * 3) = 0
print(f"{iterativeGeomSeries(x)} should be 0")  # Expected output: 0

# List with negative numbers
x = [-2, 3, -4]
# Calculation: -2 + (-2 * 3) + (-2 * 3 * -4) = -2 - 6 + 24 = 16
print(f"{iterativeGeomSeries(x)} should be 16")  # Expected output: 16

# List with a mix of integers and floats
x = [1.5, 2, 2.5]
# Calculation: 1.5 + (1.5 * 2) + (1.5 * 2 * 2.5) = 1.5 + 3 + 7.5 = 12
print(f"{iterativeGeomSeries(x)} should be 12.0")  # Expected output: 12.0

# Larger list
x = [2, 2, 2, 2, 2]
# Calculation: 2 + (2 * 2) + (2 * 2 * 2) + (2 * 2 * 2 * 2) + (2 * 2 * 2 * 2 * 2)
# = 2 + 4 + 8 + 16 + 32 = 62
print(f"{iterativeGeomSeries(x)} should be 62")  # Expected output: 62