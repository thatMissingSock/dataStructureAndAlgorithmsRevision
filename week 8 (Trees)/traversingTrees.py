from trees import *
"""
THE TREE LOOKS LIKE THIS:
                                                A
                                            B       D
                                        C         E   F
"""
# The following is test code provided by Faris
C = Tree("C")
B = join_T([C], "B")

E = Tree("E")
F = Tree("F")
D = join_T([E, F], "D")

A = join_T([B, D], "A")
print(A)
# ###################################################################################################################
def print_pre_T(root):
    """
    This function should take in a tree(root) and traverse the tree pre-order. Whilst traversing it should print out the
    current value of the leaf it is in.
    :param root: A tree (not binary).
    :return: Nothing, it should print every element as it traverses.
    """
    if root is None:
        return

    print(root.value)
    for child in root.children: # without this, the code turns the recursion into a list for some reason -_-
        tempValue = print_pre_T(child)

# The following is test code provided by Faris
def test_print_pre_T():
  print("\n\033[1m############# print_pre_T #############\033[0m\n")
  print("should show A, B, C,..., F on separate lines in order:")
  print_pre_T(A)


def putInList(root):
    """
    Converts all values of the root and its descendants into a single list.
    I created a new function just because it seemed easier than to cram it all into one function.
    :param root: A tree.
    :return: A flat list containing all the values of the root and its descendants.
    """
    if root is None:
        return []

    tempList = [root.value]  # Start with the current node's value

    # Add all values from the children recursively
    for child in reversed(root.children):
        tempList.extend(putInList(child))  # Extend instead of append as we are adding 2 lists together

    return tempList

def print_post_T(root):
    """
    This should do the same as the above function but in reverse order.
    I HAD TO REUSE 'PUTINLIST' FUNCTION TO MAKE THIS WORK.
    :param root: A tree.
    :return: Nothing, it should print every element as it traverses
    """
    tempList = putInList(root)
    for i in range(len(tempList) - 1,-1, -1):
        print(tempList[i])

# The following is test code provided by Faris
def test_print_post_T():
  print("\n\033[1m############# print_post_T #############\033[0m\n")
  print("should show C, B, E, F, D, A on separate lines in that order:")
  print_post_T(A)

def print_in_BT(root):
    """
    This function should take in a binary tree and traverse it IN ORDER whilst printing out each value as it goes along.
    :param root: A binary tree.
    :return: Nothing, it should print every element as it traverses.
    """
    if root is None:
        return

    print_in_BT(root.left_child)

    print(root.value)

    print_in_BT(root.right_child)

# The following is test code provided by Faris
"""
THE BINARY TREE LOOKS LIKE THIS:
        A
       / \
      B   D
     /   / \
    C   E   F

"""
def test_print_in_BT():
  print("\n\033[1m############# print_in_BT #############\033[0m\n")
  C = BinaryTree("C")
  B = BinaryTree("B")
  B.left_child = C
  E = BinaryTree("E")
  F = BinaryTree("F")
  D = join_BT(E, F, "D")
  A = join_BT(B, D, "A")
  print("should show C, B, A, E, D, F on separate lines in that order:")
  print_in_BT(A)

def string_T(root):
    """
    IM NOT GONNA DO THIS ONE, mainly because he does it already in the files labelled 'trees.py'.
    :param root:
    :return:
    """

# The following is test code provided by Faris
def test_string_T():
  print("\n\033[1m############# string_T #############\033[0m\n")
  print(string_T(C), " should be:\n", "C <>", sep="")
  print()
  print(string_T(D), " should be:\n", "D <E <>, F <>>", sep="")
  print()
  print(string_T(A), " should be:\n", "A <B <C <>>, D <E <>, F <>>>", sep="")
  print()


def filepaths_T(root):
  filepaths_helper(root, "/")

def filepaths_helper(root, prefix):
  current_path = prefix + root.value
  "to do"

def fib_callstack(n):
  "to do"

# The following is test code provided by Faris
def test_filepaths_T():
  print("\n\033[1m############# filepaths_T #############\033[0m\n")
  print("should print the following lines in this order:")
  print("/A/", "/A/B/", "/A/B/C", "/A/D/", "/A/D/E", "/A/D/F", sep="\n")
  print()
  filepaths_T(A)

def test_fib_callstack():
  print("\n\033[1m############# fib_callstack #############\033[0m\n")
  print(fib_callstack(0), " should be ", "fib 0 <>", sep="")
  print(fib_callstack(1), " should be ", "fib 1 <>\n", sep="")
  print(fib_callstack(2), " should be:\n", "fib 2 <fib 1 <>, fib 0 <>>\n", sep="")
  print(fib_callstack(3), " should be:\n", "fib 3 <fib 2 <fib 1 <>, fib 0 <>>, fib 1 <>>\n", sep="")
  print(fib_callstack(4), " should be:\n", "fib 4 <fib 3 <fib 2 <fib 1 <>, fib 0 <>>, fib 1 <>>, fib 2 <fib 1 <>, fib 0 <>>>\n", sep="")

test_print_pre_T()
test_print_post_T()
test_print_in_BT()
# test_string_T()
# test_filepaths_T()
# test_fib_callstack()