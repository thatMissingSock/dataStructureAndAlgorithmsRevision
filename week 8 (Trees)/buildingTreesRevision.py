from trees import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def zigzag(rootval, directions, values):
    """
    This function should take in three parameters and do the following:
    - using the parameter 'rootval', it should set this value as the root node in a BINARY TREE
    - using the parameter 'directions', it should use this list of L/R to set the values in the next parameter. As its a
    binary tree it only has a left or right child and thus should use this as a guide
    - using the parameter 'values' it should use this to set the actual elements of the binary tree
    :param rootval: A value.
    :param directions: A list of L/R values.
    :param values: A list of values.
    :return: A 'zigzagging' binary tree
    """
    tempList = [None] * (len(values) + 1)
    for i in range(len(directions) - 1 , - 1, - 1):
        if tempList[i + 1] is None:
            tempValue = values[i]
            tempList[i] = BinaryTree(tempValue)
        else:
            tempValue = values[i]
            if directions[i + 1] == 'L':
                tempList[i] = join_BT(tempList[i + 1], None, tempValue)
            elif directions[i + 1] == 'R':
                tempList[i] = join_BT(None, tempList[i + 1], tempValue)

    tempOutput = 0
    if directions[0] == 'R':
        tempOutput = join_BT(None, tempList[0], rootval)
    elif directions[0] == 'L':
        tempOutput = join_BT(tempList[0], None, rootval)

    return tempOutput


# test code provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
rootValue = 'Z'
directionList = ['L','R','L','L','R']
valueList = ['A','C','D','N','G']
print(f"{zigzag(rootValue, directionList, valueList)} and it should be:\nZ <A <None, C <D <N <None, G <>>, None>, None>>, None>")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    for child in (root.children):
        tempList.append(putInList(child))  # Extend instead of append as we are adding 2 lists together

    return tempList

def remove_value_T(root, v):
    """
    This function should take in a tree(root) and a value(v). Using this, it should remove all instances of v from the tree
    AND their descendants (think of it as pruning the branch).
    IF the root of the tree contains the value THEN YOU DO NOTHING and just return the tree.
    :param root: A tree.
    :param v: A value.
    :return: A pruned tree.
    """
    # # I decided to reuse my 'putInList' function since it seems to work so well
    # tempList = putInList(root)
    # print (tempList)




# test code provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
C = Tree("C")
B = join_T([C], "B")

E = Tree("E")
F = Tree("F")
D = join_T([E, F], "E")

A = join_T([B, D], "A")
print(A)
print(remove_value_T(A, 'E'))


def from_lists_T(lists):
  "to do"
