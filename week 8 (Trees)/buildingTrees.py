from trees import *

def join_T(trees, v):
    """
    This functions needs to take in a list of tree roots(trees) and a root value(v) and create a new root node with the
    value of v AND with all the other trees as its children.
    :param trees: A list of tree roots.
    :param v: A value.
    :return: A new tree root node.
    """
    newRoot = Tree(v) # this uses the class to intialise a new tree object
    newRoot.children = trees # inside that bit, there is a dynamic variable called children that auto initialises as empty, we explicityly state it is instead trees
    return newRoot

# The following is test code provided by Faris
def test_join_T():
    print("\n\033[1m############# join_T #############\033[0m\n")
    B = Tree("banana")
    C = Tree("cherry")
    D = Tree("durian")
    A = join_T([B, C, D], "apple")
    print(A, " should be:\n", "apple <banana <>, cherry <>, durian <>>", sep="")


def join_BT(left, right, v):
    """
    This function should take in two binary trees(left and right) and a value(v). Using these, it should create a new root
    branch with a branch made up of 'left' and a branch made up of 'right'.
    :param left: A binary tree.
    :param right: A binary tree.
    :param v: A value.
    :return: A new binary tree made up of all the values above.
    """
    newNode = BinaryTree(v)
    newNode.left_child = left
    newNode.right_child = right
    return newNode

# The following is test code provided by Faris
def test_join_BT():
    print("\n\033[1m############# join_BT #############\033[0m\n")
    B = BinaryTree("banana")
    C = BinaryTree("cherry")
    D = BinaryTree("durian")
    C.right_child = D
    A = join_BT(B, C, "apple")
    print(A, " should be:\n", "apple <banana <>, cherry <None, durian <>>>", sep="")


def replace_T(root, u, v):
    """
    This function should take in an EXISTING tree(root) and find all instances of a value(u) and replace it with a different
    value(u).
    THE ONLY WAY WE COULD THINK OF WAS TO USE RECURSION.
    :param root: A tree.
    :param u: A value to be changed.
    :param v: The new value to be inputted.
    :return: A *changed* tree.
    """
    if root is None:
        return

    if root.value == u: # this checks the 'head' to see if it is the value that we need to change
        root.value = v

    for child in root.children: # this initiates the recursion
        replace_T(child, u, v)

# The following is test code provided by Faris
def test_replace_T():
    print("\n\033[1m############# replace_T #############\033[0m\n")
    B = Tree("banana")
    C = Tree("cherry")
    B2 = Tree("banana")
    C.children = [B2]
    A = join_T([B, C], "apple")
    replace_T(A, "banana", "berry")
    print(A, " should be:\n", "apple <berry <>, cherry <berry <>>>", sep="")

def deepcopy_T(root):
    """
    This function should take in a tree(root) and start by making a 'deep copy' (I think he means one that is not aliased).
    It should do this by first making the value the same as the OG then RECURSIVELY make copies of all the children of
    root.
    :param root: A tree.
    :return: A new deep copy of root but done recursively.
    """
    if root is None:
        return

    newNode = Tree(root.value)

    for child in root.children:
        newNode.children.append(deepcopy_T(child))

    return newNode




# The following is test code provided by Faris
def test_deepcopy_T():
    print("\n\033[1m############# deepcopy_T #############\033[0m\n")
    B = Tree("banana")
    C = Tree("cherry")
    D = Tree("durian")
    A = join_T([B, C, D], "apple")
    A2 = deepcopy_T(A)
    print(A2, " should be:\n", "apple <banana <>, cherry <>, durian <>>", sep="")

def insert_left_BT(root, v):
    """
    This function should take in an existing binary tree(root) and a value(v). It should then insert a new node inside the
    left branch of the binary tree, the node should have a value of v.
    IF the left branch of root already has a tree, then it should set that existing branch to be the LEFT CHILD of the new
    node.
    :param root: A binary tree.
    :param v: A value.
    :return: The same binary tree but with v implemented as its left child.
    """
    if root.left_child == None: # if statement to check if there is NO BRANCH
        tempNode = BinaryTree(v)
        root.left_child = tempNode
        return root
    else: # if state incase THERE IS A BRANCH
        tempBranch = root.left_child
        newBinaryTree = BinaryTree(v)
        newBinaryTree.left_child = tempBranch
        root.left_child = newBinaryTree
        return root


# The following is test code provided by Faris
def test_insert_left_BT():
    print("\n\033[1m############# insert_left_BT #############\033[0m\n")
    C = BinaryTree("cherry")
    insert_left_BT(C, "strawberry")
    print(C, " should be:\n", "cherry <strawberry <>, None>", sep="")

    B = BinaryTree("banana")
    D = BinaryTree("durian")
    B.right_child = D
    insert_left_BT(B, C)
    print()
    print(B, " should be:\n", "banana <cherry <strawberry <>, None> <>, durian <>>", sep="")

def all_right_BT(x):
    """
    This function should take in a list of values(x) and given this list, it should create a binary tree with x[0] as the
    root. Any other value should then become the RIGHT branch.
    So x[1] is the right child, x[2] is the right grandchild, x[3] is the right great-grandchild ad so on and so forth.
    After thinking about it, RECURSION seems to be the best bet.
    :param x: A list of values.
    :return: A binary tree containing ONLY right branches.
    """
    if len(x) == 1:
        head = x[0]
        tempNode = BinaryTree(head)
        return tempNode

    head = x[0]
    tail = x[1:]
    tempNode = BinaryTree(head)

    # the following line I had to get from GPT, something to do with the syntax
    tempNode.right_child = all_right_BT(tail)

    # tempNode.right_child(all_right_BT(tail))
    return tempNode


# The following is test code provided by Faris
def test_all_right_BT():
    print("\n\033[1m############# all_right_BT #############\033[0m\n")
    print(all_right_BT(["apple"]), " should be:\n", "apple <>", sep="")
    print(all_right_BT(["apple", "banana"]), " should be:\n", "apple <None, banana <>>", sep="")
    print(all_right_BT(["apple", "banana", "cherry"]), " should be:\n", "apple <None, banana <None, cherry <>>>",
          sep="")


test_join_T()
test_join_BT()
test_replace_T()
test_deepcopy_T()
test_insert_left_BT()
test_all_right_BT()
