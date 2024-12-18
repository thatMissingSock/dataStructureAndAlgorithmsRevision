###################################
class LStack:
    def __init__(new_stack):
        """
        You use this to initialise that you're creating a new stack, it MUST always start empty as the parameters only
        take in nothing (itself).
        """
        new_stack._contents = []

    def push(stack, value):
        """
        This is when we add values/elements to the stack
        :param value: Whatever we are adding.
        :return: An updated stack with the new values.
        """
        stack._contents.append(value)

    def top(stack):
        """
        This is a function we call when we want to see the top of the stack.
        :return: The value at the top (next in line to be removed).
        """
        return stack._contents[-1]

    def pop(stack):
        """
        This is what we use to remove elements from the stack. Because of the nature of the stack we can only take of the
        top [-1] of the stack.
        :return: A value/element that was at the top of the stack, WE DO NOT GET THE STACK AS THE RETURNED VALUE BUT IT IS
        UPDATED!
        """
        top = stack.top()
        del stack._contents[-1]
        return top

    def count(stack):
        """
        This is what we use to count the number of values inside the stack.
        :return: The number of elements inside the stack (i.e. its length).
        """
        return len(stack._contents)

    # Just so we can print a stack
    def __str__(stack):
        """
        This just converts the stack into a printable string literal, for some reason the format is |(the elements)>.
        :return: A string literal representation of the stack.
        """
        # Change bracket appearance to |--->
        return f"|{str(stack._contents)[1:-1]}>"

    def __repr__(stack):
        """
        Just the final continuation of the above str function, it prints it out when asked.
        :return: Printed string literal.
        """
        return __str__(stack)
    ###################################


# For this exercise, only use the ADT methods above.
# Don't access _contents directly!


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def push_all(s, x):
    """
    WE CAN ONLY USE THE ADT METHODS ABOVE.
    This should iterate through all the values in the list(x) and add them to the already existing stack(s).
    :param s: A stack.
    :param x: A list of values.
    :return: A stack updated with the list of values.
    """
    for i in range(len(x)):
        LStack.push(s, x[i])

    return s

# test code provided by me :)
# Test push_all
s1 = LStack()
push_all(s1, [1, 2, 3])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{s1} and it should be |1, 2, 3>")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pop_all(s):
    """
    This should count all of the elements in the stack and then return a new list with all of the elements popped.
    Because of the nature of stacks, the top element (n = -1) should be the first place in the new list (n = 0).
    :param s: A stack
    :return: A new list containing all of the elements in s.
    """
    tempOutput = [None] * LStack.count(s)
    for i in range(len(tempOutput)):
        tempOutput[i] = LStack.pop(s)

    return tempOutput

# test code provided by me
# Test pop_all
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
s2 = LStack()
push_all(s2, [4, 5, 6])
result_pop_all = pop_all(s2)
print()
print(f"{result_pop_all} and it should be [6, 5, 4]")
print(f"{s2} and it should be |>, this just checks that the original stack is empty as we popped all of the elements")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def reverse_new(s):
    """
    This should take in a stack(s) and return a new stack that is the same as the orignal(s) but with the elements in reverse
    order. If we was to print the orignal stack it SHOULD return empty (he doesn't say this but doesn't say not to so
    I'm going to assume we are).
    :param s: A stack.
    :return: A new stack with the elements in reverse order.
    """
    tempStack = LStack()
    for i in range(LStack.count(s)):
        tempValue = LStack.pop(s)
        LStack.push(tempStack, tempValue)
    return tempStack

# test code provided by me :P
# Test reverse_new
s3 = LStack()
push_all(s3, [7, 8, 9])
reversed_stack = reverse_new(s3)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{reversed_stack} and it should be |9, 8, 7>")
print(f"{s3} and it should be |>")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def reverse_same(s):
    """
    This is the same as above but instead of creating a new stack we should return the same stack.
    :param s: A stack.
    :return: The SAME stack but with the elements in reverse order.
    """
    # I'm just going to use the function we created above because why not
    tempList = pop_all(s)
    for i in range(len(tempList)):
        LStack.push(s, tempList[i])

    return s

# test code provided by me :0
# Test reverse_same
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
s4 = LStack()
push_all(s4, [10, 11, 12])
reverse_same(s4)
print(f"{s4} when it should be |12, 11, 10>")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def transfer(s1, s2):
    """
    This should transfer the values from the first stack(s1) to the second stack(s2) WITHOUT inverting their order.
    :param s1: A stack.
    :param s2: A second stack.
    :return: The stacks should return but with transfered elements.
    """
    tempList1 = [None] * LStack.count(s1)
    tempList2 = [None] * LStack.count(s2)

    # the following is just to put the contents of both the stacks into tempLists IN THE SAME ORDER
    count = 0
    for i in range(len(tempList1)):
        tempList1[((len(tempList1) - 1) - count)] = LStack.pop(s1)
        count += 1

    count = 0
    for i in range(len(tempList2)):
        tempList2[((len(tempList2) - 1) - count)] = LStack.pop(s2)
        count += 1

    # now we just need to put them into the other stack
    push_all(s1, tempList2)
    push_all(s2, tempList1)


# test code provided by me :(
# Test transfer
s5 = LStack()
s6 = LStack()
push_all(s5, [13, 14, 15])
push_all(s6, [1, 2, 3, 4, 5])
transfer(s5, s6)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{s5} when it should be |1, 2, 3, 4, 5>")  # s5 should have s6 contents
print(f"{s6} when it should be |13, 14, 15>")  # s6 has s5's contents


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert_below(s1, s2):
    """
    This function should take in two stacks (s1 and s2) and implement all of the elements found in s1 underneath s2.
    He does not state if he wanted a new stack...so we are going to assume we return s2 but updated.
    This means that it should return like this s2 = (s1Elements, s2Elements).
    :param s1: A stack.
    :param s2: A stack.
    :return: s2 bit with s1 beneath it all.
    """
    tempList = [None] * (LStack.count(s1) + LStack.count(s2))
    count = 0
    for i in range(LStack.count(s2)):
        tempList[((len(tempList) - 1) - count)] = LStack.pop(s2)
        count += 1

    for i in range(LStack.count(s1)):
        tempList[((len(tempList) - 1) - count)] = LStack.pop(s1)
        count += 1

    push_all(s2, tempList)



# test code provided by me -_-
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test insert_below
s7 = LStack()
s8 = LStack()
push_all(s7, [16, 17])
push_all(s8, [18, 19])
insert_below(s7, s8)
print(f"{s8} when it should be |16, 17, 18, 19>")  # s7 inserted beneath s8
print(f"{s7} when it should be |>") # should be empty since we popped it all


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def extract(s, v):
    """
    This function should look for a value(v) inside a stack(s) and return the stack without that value.
    If the value is not found, then we do nothing. The stack should be returned as normal just without that value.
    He did not mention what we do if there are multiples of this value...so for this question, we assume that we are extracting
    ALL the elements that match that value.
    :param s: A stack.
    :param v: A value.
    :return: A stack with that value removed.
    """
    count = 0
    numberOfV = 0
    tempList = [None] * LStack.count(s)
    for i in range(len(tempList)):
        tempList[((len(tempList) - 1) - count)] = LStack.pop(s)
        count += 1
        if tempList[i] == v:
            numberOfV += 1

    if numberOfV != 0:
        for i in range(numberOfV + 1):
            tempList.remove(v)

    push_all(s, tempList)


# test code provided by me :X
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test extract
s9 = LStack()
push_all(s9, [22, 20, 21, 22, 22, 23, 22])
extract(s9, 22)
print(f"{s9} when it should be |20, 21, 23>")  # 22 removed


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def duplicate(s):
    """
    This should just take in a stack(s) and return a new stack that is EXACTLY the same as the first stack. The first
    stack should remain unchanged.
    :param s: A stack.
    :return: A new duplicate stack.
    """
    tempList = [None] * LStack.count(s)
    count = 0
    for i in range(len(tempList)):
        tempList[((len(tempList) - 1) - count)] = LStack.pop(s)
        count += 1

    newStack = LStack()
    push_all(s, tempList)
    push_all(newStack, tempList)
    return newStack

# test code provided by me :)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test duplicate
s10 = LStack()
push_all(s10, [24, 25, 26])
duplicated_stack = duplicate(s10)
print(f"{duplicated_stack} when it should be |24, 25, 26>")
print(f"{s10} when it should still be |24, 25, 26>")  # Original stack unchanged