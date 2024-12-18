
###################################
class LStack:
    def __init__(new_stack):
        new_stack._contents = []

    def push(stack, value):
        stack._contents.append(value)

    def top(stack):
        return stack._contents[-1]

    def pop(stack):
        top = stack.top()
        del stack._contents[-1]
        return top

    def count(stack):
        return len(stack._contents)

    # Just so we can print a stack
    def __str__(stack):
        # Change bracket appearance to |--->
        return f"|{str(stack._contents)[1:-1]}>"

    def __repr__(stack):
        return __str__(stack)
    ###################################


# Only use the ADT methods above.
# Don't access _contents directly.

def check_brackets(s):
    """
    WE CAN ONLY USE THE ADT METHODS FROM STACK.
    This function should take in a list of lists(s), and if the brackets are in pairs (it should check if the brackets are
    closed). IT IS FINE if the brackets are closed, but there is a number before or after the brackets.
    STRING LITERALS ARE CONSIDERED LISTS.
    I THINK (he doesn't say) that we need to make them into stacks within this function to then do the question...long-winded
    I know.
    :param s: A list of lists.
    :return: A boolean based on if all the brackets are closed.
    """

    # the following is just to make it into a stack
    tempStack = LStack()

    for i in range(len(s)):
        LStack.push(tempStack, s[i])

    stackCount = LStack.count(tempStack)

    rightBracketCount = 0
    leftBracketCount = 0

    for i in range(stackCount):
        tempValue = LStack.pop(tempStack)
        if tempValue == ')':
            rightBracketCount += 1
        if tempValue == '(':
            leftBracketCount += 1

    if leftBracketCount == rightBracketCount:
        return True
    else:
        return False


# test code provided by Faris O.o

# "(2 + 2)"
x = ["(", "2", "+", "2", ")"]

print(check_brackets(x), "should be", True)

# "(2 + 2" as above, without final ")"
y = x[:-1]
print(check_brackets(y), "should be", False)

# "1 + 1"
x = ["1", "+", "1"]
print(check_brackets(x), "should be", True)

# "1 + (2 + (3 + (4)) + 5)"
s = "1 + ( 2 + ( 3 + ( 4 ) ) + 5 )"
x = s.split()
print(check_brackets(x), "should be", True)

# "1 + (2 + (3 + (4) + 5)" missing one ")"
s = "1 + ( 2 + ( 3 + ( 4 ) + 5 )"
x = s.split()
print(check_brackets(x), "should be", False)


# "2 + (3 + (4)) + 5)" missing one "("
s = "2 + ( 3 + ( 4 ) ) + 5 )"
x = s.split()
print(check_brackets(x), "should be", False)