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

def follow(t, s):
    """
    This function should take in a root of a tree(t) and a list of steps(s) consisting of either 'left' or 'right'. Using
    this it should follow down the tree as far as possible and then return the value at the base.
    :param t: A tree.
    :param s: A list of directions.
    :return: A value.
    """

    tempList = [None] * len(s)

    for i in range(len(s)):
        if i == 0:
            if s[i] == 'left':
                tempList[i] = t.left_child
            elif s[i] == 'right':
                tempList[i] = t.right_child
        else:
            if s[i] == 'left':
                tempList[i] = tempList[i - 1].left_child
            elif s[i] == 'right':
                tempList[i] = tempList[i - 1].right_child

    if tempList[-1] is not None:
        return tempList[-1].value
    else:
        return None


# test code provided by GPT, reviewed by me :P
# Test `follow`
def test_follow():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("\033[1mTesting follow\033[0m")
    root = BinaryTree(10)
    root.left_child = BinaryTree(5)
    root.right_child = BinaryTree(15)
    root.left_child.left_child = BinaryTree(3)
    root.left_child.right_child = BinaryTree(7)
    print(root)
    print(follow(root, ["left", "left"]), " should be 3")  # Follows left -> left
    print(follow(root, ["left", "right"]), " should be 7")  # Follows left -> right
    print(follow(root, ["right"]), " should be 15")  # Follows right
    print(follow(root, ["left", "left", "right"]), " should be None")  # Out of bounds


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def in_range(t, low, high):
    """
    This function needs to take in a non-binary tree(t) and two values(low and high). Using these, it should return a True
    if all of the values inside the tree are inside the range (in this format: low <= v <= high).
    :param t: A non-binary tree.
    :param low: A value.
    :param high: A value.
    :return: A boolean value.
    """

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
        for child in root.children:
            tempList.extend(putInList(child))  # Extend instead of append as we are adding 2 lists together

        return tempList
    tempList = putInList(t)

    booleanOutput = True
    for i in range(len(tempList)):
        if tempList[i] < low or tempList[i] > high:
            booleanOutput = False
            break
    return booleanOutput


# test code provided by GPT, reviewed by me :P
# Test `in_range`
def test_in_range():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    root = Tree(10)
    root.children = [Tree(5), Tree(15)]
    root.children[0].children = [Tree(3), Tree(7)]
    root.children[1].children = [Tree(12), Tree(20)]

    print(in_range(root, 3, 20), " should be True")  # All values are in range
    print(in_range(root, 5, 15), " should be False")  # 3 and 20 are out of range
    print(in_range(root, 1, 25), " should be True")  # Wide range includes all values


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def in_range_v2(t, low, high):
    """
    This function should do the same as the above but with one MAJOR change. If either of the limits are none then it is
    simply ignored, and you test for the other limit.
    If both are None, then you return True.
    :param t: A non-binary tree.
    :param low: A value.
    :param high: A value.
    :return: A boolean value.
    """
    booleanOutput = True

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
        for child in root.children:
            tempList.extend(putInList(child))  # Extend instead of append as we are adding 2 lists together

        return tempList

    tempList = putInList(t)

    if low != None and high != None:

        for i in range(len(tempList)):
            if tempList[i] < low or tempList[i] > high:
                booleanOutput = False
                break
        return booleanOutput

    elif low == None and high != None:

        for i in range(len(tempList)):
            if tempList[i] > high:
                booleanOutput = False
                break

    elif low != None and high == None:

        for i in range(len(tempList)):
            if tempList[i] < low:
                booleanOutput = False
                break

    elif low == None and high == None:
        booleanOutput = True

    return booleanOutput

# test code provided by GPT, reviewed by me :P
# Test `in_range_v2`
def test_in_range_v2():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("\n\033[1mTesting in_range_v2\033[0m")
    root = Tree(10)
    root.children = [Tree(5), Tree(15)]
    root.children[0].children = [Tree(3), Tree(7)]
    root.children[1].children = [Tree(12), Tree(20)]

    print(in_range_v2(root, None, 20), " should be True")  # Only checks upper limit
    print(in_range_v2(root, 5, None), " should be False")  # Only checks lower limit
    print(in_range_v2(root, None, None), " should be True")  # No limits to check


# Run all tests
test_follow()
test_in_range()
test_in_range_v2()

