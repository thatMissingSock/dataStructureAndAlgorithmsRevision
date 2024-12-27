###################################
class LBStack:
    def __init__(new_stack, capacity):
        new_stack._contents = capacity * [None]
        new_stack._count = 0

    def push(stack, value):
        stack._contents[stack._count] = value
        stack._count += 1

    def top(stack):
        return stack._contents[stack._count - 1]

    def pop(stack):
        top = stack.top()
        stack._contents[stack._count - 1] = None
        stack._count -= 1
        return top

    def count(stack):
        return stack._count

    def is_full(stack):
        "to do"

  # Just so we can print a stack
    def __str__(stack):
      # Change bracket appearance to |--->
     return f"|{str(stack._contents)[1:-1]}>"

    def __repr__(stack):
        return __str__(stack)
###################################


tempStack = LBStack(7)
LBStack.push(tempStack, 1)
LBStack.push(tempStack,2)
LBStack.push(tempStack,3)
LBStack.push(tempStack,4)
LBStack.pop(tempStack)

print(tempStack)

