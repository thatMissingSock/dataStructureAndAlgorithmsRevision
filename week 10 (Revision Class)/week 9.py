#####################################################
class BinaryTree:
    def __init__(new_tree, v):
        new_tree.value = v
        new_tree.left_child = None
        new_tree.right_child = None

    def __str__(root):
        s = str(root.value)
        s += " <"
        child_strings = []
        left = root.left_child
        right = root.right_child
        if left != None or right != None:
            child_strings.append(str(left))
            child_strings.append(str(right))
        s += ", ".join(child_strings)
        s += ">"
        return s

    def __repr__(root):
        return str(root)


class Tree:
    def __init__(new_tree, v):
        new_tree.value = v
        new_tree.children = []

    def __str__(root):
        s = str(root.value)
        s += " <"
        child_strings = []
        for child in root.children:
            child_strings.append(str(child))
        s += ", ".join(child_strings)
        s += ">"
        return s

    def __repr__(root):
        return str(root)


#####################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def min(t):
    """
    This function should take in a binary tree(t) and return the minimum value in said tree.
    :param t: A binary tree.
    :return: The minimum value in the tree.
    """

    def putInListBST(root):
        if root is None:
            return []
        return [root.value] + putInListBST(root.left_child) + putInListBST(root.right_child)

    tempList = putInListBST(t)

    min = None
    for i in range(len(tempList)):
        if min == None:
            min = tempList[i]
        elif tempList[i] < min:
            min = tempList[i]

    return min


# test code provided by GPT but reviewed by me :-)
# Test `min`
def test_min():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    root = BinaryTree(10)
    root.left_child = BinaryTree(5)
    root.right_child = BinaryTree(15)
    root.left_child.left_child = BinaryTree(3)
    root.left_child.right_child = BinaryTree(7)

    print(min(root), " should be 3")  # Minimum value is in the leftmost node


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def succ(t):
    """
    This function should take in a binary tree(t) and return the successor of the root. The successor is ALWAYS the left-most
    node of the right child.
    :param t: A binary tree.
    :return: A value which represents the successor.
    """
    successorFound = False
    count = 0
    tempList = []
    while successorFound == False:
        if count == 0:
            tempList.append(t.right_child)
            count += 1
        else:
            if tempList[count - 1] is not None:
                tempList.append(tempList[count - 1].left_child)
                count += 1
            else:
                successorFound = True

    return tempList[-2].value

# test code provided by GPT but reviewed by me :-)
# Test `succ`
def test_succ():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    root = BinaryTree(10)
    root.left_child = BinaryTree(5)
    root.right_child = BinaryTree(15)
    root.left_child.left_child = BinaryTree(3)
    root.left_child.right_child = BinaryTree(7)
    root.right_child.left_child = BinaryTree(12)
    root.right_child.right_child = BinaryTree(20)

    print(succ(root), " should be 12")  # The successor of 10 is the leftmost node in the right subtree
    print(succ(root.left_child), " should be 7")  # The successor of 5 is its right child

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check(t):
    """
    This function is similar to 'in_range_v2'.
    This function should take in a binary tree(t) and return True if it is a binary search tree and False if not.
    This means that it follows the following rules:
    - the left child node should be less than the parent node
    - the right child node should be greater than or equal to the parent node
    :param t: A binary tree.
    :return: A boolean value.
    """
    outputBoolean = True

    def putInListBST(root):
        if root is None:
            return []
        return [root.value] + [putInListBST(root.left_child) + putInListBST(root.right_child)]
    tempList = putInListBST(t)
    print(tempList)


# test code provided by GPT but reviewed by me :-)
# Test `check`
def test_check():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Valid BST
    root = BinaryTree(10)
    root.left_child = BinaryTree(5)
    root.right_child = BinaryTree(15)
    root.left_child.left_child = BinaryTree(3)
    root.left_child.right_child = BinaryTree(7)
    root.right_child.left_child = BinaryTree(2)

    print(check(root), " should be True")  # Valid BST

    # Invalid BST
    root = BinaryTree(10)
    root.left_child = BinaryTree(15)  # This violates the BST property
    root.right_child = BinaryTree(5)

    print(check(root), " should be False")  # Invalid BST


# Run all tests
test_min()
test_succ()
test_check()
