"""
There was an issue with this, he imports from a file called "stack_and_queue" and ***maybe*** it works inside codio
but, I don't have access to it here so I will put the code for a queue and a stack and use it in his example so his
DFS works?
"""

# THE FOLLOWING IS THE CODE FOR AN OBJECT-QUEUE
###################################
class Queue:
  def __init__(new_queue): # this initialises a new object is made, IT MUST START EMPTY
    new_queue._contents = []

  def enqueue(queue, value): # we use this to add contents to the queue
    queue._contents.append(value)

  def front(queue): # we use this to check what the next element to be removed is (usually n = 0)
    return queue._contents[0]

  def dequeue(queue): # we use this to return the next element whilst also updating the queue
    front = queue.front()
    del queue._contents[0]
    return front

  def count(queue): # we use this to count how many elements there are in the queue
    return len(queue._contents)

  # Just so we can print a queue
  def __str__(queue):
    #Just change bracket appearance to <---<
    return f"<{str(queue._contents)[1:-1]}<"
  def __repr__(queue):
    return __str__(queue)
###################################

# THE FOLLOWING IS THE CODE FOR AN OBJECT-STACK
###################################
class Stack:
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


def dfs(L, v):
  """
  This function takes in an adjacency list that is linked to an unweighted tree(L) and an integer(v) that is used
  to check which node to start the traversal on.
  DFS in general is depth-first search which means it goes down the tree as opposed to going along the tree.
  :param L: An adjacency list.
  :param v: An integer,
  :return:
  """
  n = len(L) # this tells us the total number of nodes
  visited = [False] * n # we want to visit ALL of the nodes eventually so we can initialise a list to hold the values of
                        # the nodes we have visited
  results = [] # results is initialised as empty
  to_visit = Stack() # the next to visit is initialised as a stack object
  to_visit.push(v) # we add the first node to this object

  while to_visit.count() > 0: # a while loop to ensure we visit them all
    visit_next = to_visit.pop() # we pop the next node to be checked whilst temporarily storing it in a new variable

    if not visited[visit_next]: # we check to make sure the popped node is NOT already in the visited list
      # print("Visiting vertex", visit_next)
      results.append(visit_next) # we add this node we are checking to the "results" list
      visited[visit_next] = True
      neighbours = L[visit_next]
      neighbours.reverse() # <- just so they are visited in a natural looking order. Can remove for BFS.
      for u in neighbours:
        if not visited[u]:
          to_visit.push(u)
      # print("Stack is now:", to_visit)
  return results

# Simple tree: 1 <- 0 -> 2
L0 = [
  [1, 2],
  [],
  []
]
print(dfs(L0, 0), "should be:", [0, 1, 2])

# Bigger tree
L1 = [
  [1, 4, 7],
  [2, 3],
  [],
  [],
  [5, 6],
  [],
  [],
  [8, 9],
  [],
  []
]
print(dfs(L1, 0), "should be:", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Same tree as L1 but with some extra edges
L2 = [
  [1, 4, 7],
  [2, 3],
  [2],
  [3],
  [5, 6],
  [6],
  [5],
  [8, 9],
  [9],
  [9]
]
print(dfs(L2, 0), "should be:", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# THIS IS THE ACTUAL QUESTION, TO CREATE A WORKING BFS FUNCTION

def bfs(L, v):
  """
  The aim of this function is to take in an adjacency matrix(L) and an integer to act as the starting node(v) and
  go through the tree made from the list and return the possible paths but in BFS (breadth-first-search).
  :param L: An adjacency list.
  :param v: An integer.
  :return: A path of nodes that you can go through.
  """
  numberOfNodes = len(L)
  visited = [False] * numberOfNodes
  results = []

  toVisit = Queue()
  toVisit.enqueue(v)

  while toVisit.count() > 0: # a while loop to ensure we visit them all
    visit_next = toVisit.dequeue() # we pop the next node to be checked whilst temporarily storing it in a new variable

    if not visited[visit_next]: # we check to make sure the popped node is NOT already in the visited list
      # print("Visiting vertex", visit_next)
      results.append(visit_next) # we add this node we are checking to the "results" list
      visited[visit_next] = True
      neighbours = L[visit_next]
      for u in neighbours:
        if not visited[u]:
          toVisit.enqueue(u)
      # print("Stack is now:", to_visit)
  return results

# Simple tree: 1 <- 0 -> 2
L0 = [
  [1, 2],
  [],
  []
]
print(bfs(L0, 0), "should be:", [0, 1, 2])

# Bigger tree
L1 = [
  [1, 4, 7],
  [2, 3],
  [],
  [],
  [5, 6],
  [],
  [],
  [8, 9],
  [],
  []
]
print(bfs(L1, 0), "should be:", [0, 1, 4, 7, 2, 3, 5, 6, 8, 9])

# Same tree as L1 but with some extra edges
L2 = [
  [1, 4, 7],
  [2, 3],
  [2],
  [3],
  [5, 6],
  [6],
  [5],
  [8, 9],
  [9],
  [9]
]
print(bfs(L2, 0), "should be:", [0, 1, 4, 7, 2, 3, 5, 6, 8, 9])