
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_frac(x):
    """
    This should sort by the total of the fractions (x[0]/x[1]) in ascending order.'
    :param x: A list of lists.
    :return: A sorted list.
    """
    return sorted(x, key=lambda y: (y[0]/y[1]))

print(f"{sort_frac([[1, 2], [2, 5], [1, 3], [1, 4]])} should be \n[[1, 4], [1, 3], [2, 5], [1, 2]]\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_max(x):
    """
    This should sort by the max value in each nested list.
    :param x: A list of lists.
    :return: A sorted list.
    """
    return sorted(x, key=lambda y: max(y))

print(f"{sort_max([[3, 1], [2], [1, 1, 5], [2, 4]])} should be \n[[2], [3, 1], [2, 4], [1, 1, 5]]\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_count(x):
    """
    This should sort by the number of words in each string literal in ascending order.
    :param x: A list of string literals.
    :return: A sorted list.
    """
    tempList = sorted(x, key=lambda y: len(y.split()))
    return tempList

print(f"{sort_count(["bat man", "ant", "aardvark r us"])} should be\n[\"ant\", \"bat man\", \"aardvark r us\"]\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_vowel(x):
    """
    This should sort the list based on how many vowels are actually inside each string literal in ascending order.
    :param x: A list of strings.
    :return: A sorted list.
    """
    def countVowel(word):
        """
        This function essentially iterates through each character in a string literal and returns the number of vowels
        found in that string literal.
        :param word: A string literal.
        :return: The number of vowels in the string literal.
        """
        count = 0
        vowels = ["a", "e", "i", "o", "u"]
        for letterCheck in range(len(word)):
            for vowelCheck in range(len(vowels)):
                if word[letterCheck] == vowels[vowelCheck]:
                    count += 1
                    break
        return count

    return sorted(x, key=countVowel)

print(f"{sort_vowel(["octopus", "to", "teepee", "doe"])} should be \n[\"to\", \"doe\", \"octopus\", \"teepee\"]\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_rowfirst(x):
    """
    This should take in a matrix(x) and return a sorted list based on the value of the first column in each row in
    ascending order.
    :param x: A matrix.
    :return: A sorted matrix
    """
    return sorted(x, key=lambda y: y[0])

print(f"{sort_rowfirst([[9, 1, 1], [50, 0, 0], [1, 1, 8]])} should be \n[[1, 1, 8], [9, 1, 1], [50, 0, 0]]\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_rowsum(x):
    """
    This should take in a matrix (x) and sort the rows based on the sum of the values in each row in ascending order.
    :param x: A matrix.
    :return: A sorted matrix.
    """
    def rowSum(row):
        tempSum = 0
        for column in range(len(row)):
            tempSum += row[column]
        return tempSum
    return sorted(x, key=rowSum)

print(f"{sort_rowsum([[9, 1, 1], [50, -50, 9], [1, 1, 8]])} should be\n[[50, -50, 9], [1, 1, 8], [9, 1, 1]]\n")

