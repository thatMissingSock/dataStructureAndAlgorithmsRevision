###################################
class LQueue:
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

# For this exercise, only use the ADT methods above.
# Don't access _contents directly!

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def enqueue_all(q, x):
    """
    This function should take in a queue(q) and a list of values(x) and add the list of values into the queue. KEEP IN MIND
    that queues are FIFO (first in first out).
    :param q: A queue.
    :param x: A list of elements.
    :return: An updated queue.
    """
    for i in range(len(x)):
        LQueue.enqueue(q, x[i])


# test code provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test enqueue_all
q1 = LQueue()
enqueue_all(q1, [1, 2, 3])
print(f"{q1} when it should be <1, 2, 3<")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dequeue_all(q):
    """
    This function should take in a queue and put all of the elements in a list.
    :param q: A queue.
    :return: A new list containing all the elements of the queue.
    """
    tempList = [None] * LQueue.count(q)
    for i in range(len(tempList)):
        tempList[i] = LQueue.dequeue(q)

    return tempList

# test code provided by me :P
print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test dequeue_all
q2 = LQueue()
enqueue_all(q2, [4, 5, 6])
result_dequeue_all = dequeue_all(q2)
print(f"{result_dequeue_all} when it should be [4, 5, 6]")
print(f"{q2} when it should be <<")  # Queue is now empty

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cycle(q, n):
    """
    This function should take in a queue(q) and an integer(n) and shift the elements within that queue n amount of times.
    So if 1 was at index 0, then its new place should be at index 0 + n.
    IF THE NEW INDEX IS BIGGER THAN THE SIZE OF THE LIST, then of course we just cycle back to the front.
    :param q: A queue.
    :param n: An integer.
    :return: A cycled queue.
    """
    tempList = dequeue_all(q)

    cycledTempList = [None] * len(tempList)

    for i in range(len(cycledTempList)):
        if i + n <= (len(cycledTempList) - 1):
            cycledTempList[i + n] = tempList[i]
        elif i + n > (len(cycledTempList) - 1):
            cycledTempList[(i + n) - len(cycledTempList)] = tempList[i]

    enqueue_all(q, cycledTempList)

# test code provided by me :O
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test cycle
q3 = LQueue()
enqueue_all(q3, [7, 8, 9, 10])
cycle(q3, 2)
print(f"{q3} when it should be <9, 10, 7, 8<")  # First 2 elements cycled to the back


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def reverse(q):
    """
    This function should take in a queue and reverse the order of the elements in the queue. WE SHOULD NOT MAKE A NEW
    STACK.
    :param q: A queue.
    :return: A queue with reverse order.
    """
    tempList = dequeue_all(q)

    reversedTempList = list(reversed(tempList))

    enqueue_all(q,reversedTempList)

# test code provided by me :X
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test reverse
q4 = LQueue()
enqueue_all(q4, [11, 12, 13])
reverse(q4)
print(f"{q4} when it should be <13, 12, 11<")  # Order reversed

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def transfer(q1, q2):
    """
    This function should take in two queues(q1 and q2) and transfer the elements between each other. He does not state it
    so we assume that they transfer the elements between each other and NEITHER queue should be empty.
    :param q1: A queue.
    :param q2: A queue.
    :return: q1 == q2 and q2 == q1
    """
    tempList1 = dequeue_all(q1)
    tempList2 = dequeue_all(q2)

    enqueue_all(q1, tempList2)
    enqueue_all(q2, tempList1)


# test code provided by duff-man
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test transfer
q5 = LQueue()
q6 = LQueue()
enqueue_all(q5, [14, 15, 16])
enqueue_all(q6, [1, 2, 3])
transfer(q5, q6)
print(f"{q5} when it should be <1, 2, 3<")  # q5 contains all of q6's elements
print(f"{q6} when it should be <14, 15, 16<")  # q6 contains all of q5's elements

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert_front(q1, q2):
    """
    This function should take in two queues(q1 and q2) and return q2 but with all the elements from q1 in front of
    the elements of q2.
    So it should return q2 = (q1Elements, q2Elements)
    :param q1: A queue.
    :param q2: A queue.
    :return: An updated q2 with all the elements of q1 infront.
    """
    tempList = dequeue_all(q1)
    tempList += dequeue_all(q2)

    enqueue_all(q2, tempList)


# test code provided by me :P
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test insert_front
q7 = LQueue()
q8 = LQueue()
enqueue_all(q7, [17, 18])
enqueue_all(q8, [19, 20])
insert_front(q7, q8)
print(f"{q8} when it should be <17, 18, 19, 20<")  # q7 inserted at the front of q8
print(f"{q7} when it should be <<") # this one should be emptied

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def extract(q, v):
    """
    This function should take in a queue(q) and a value(v) and return the same queue, but with all of those elements removed.
    He does not state if we should just remove one or all of them so we are going to assume all of them.
    IF THE VALUE IS NOT FOUND, then we just return q unchanged :)
    :param q: A queue.
    :param v: A value.
    :return: A queue without any instances of v.
    """
    tempList = dequeue_all(q)

    count = 0
    for i in range(len(tempList)):
        if tempList[i] == v:
            count += 1

    if count > 0:
        for j in range(count):
            tempList.remove(v)

    enqueue_all(q, tempList)


# test code provided by moi
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test extract
q9 = LQueue()
enqueue_all(q9, [22, 22, 22, 21, 22, 23, 24, 22, 22, 22])
extract(q9, 22)
print(f"{q9} when it should be <21, 23, 24<")  # 23 removed

# Note: Adjust implementation of `extract` to handle non-existing values gracefully
extract(q9, 99)
print(f"{q9} when it should still be <21, 22, 24<")  # Unchanged if value not found