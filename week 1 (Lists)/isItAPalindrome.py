
def is_pali(x):
    """
    It should check if the string literal is a palindrome or not.
    :param x: A string
    :return: True or False depending on if it meets the conditions
    """
    result = True
    tempLen = (len(x) -1)
    for i in range(len(x)):
        if i != tempLen:
            if x[i] != x[tempLen]:
                result = False
        tempLen -= 1
    return result

# test code below
s = "ABBA"
print(is_pali(s), "should be True")

s = "ABBD"
print(is_pali(s), "should be False")

s = "step on no pets"
print(is_pali(s), "should be True")

s = "kayak deed rotator deed kayak"
print(is_pali(s), "should be True")

s = "tomatotamot"
print(is_pali(s), "should be True")

s = "Woo young-woo"
print(is_pali(s), "should be False")

s = "a"
print(is_pali(s), "should be True")