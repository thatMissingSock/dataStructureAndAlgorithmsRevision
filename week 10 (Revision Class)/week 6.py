###################################
class Queue:
  def __init__(new_queue):
    new_queue._contents = []

  def enqueue(queue, value):
    queue._contents.append(value)

  def front(queue):
    return queue._contents[0]

  def dequeue(queue):
    front = queue.front()
    del queue._contents[0]
    return front

  def count(queue):
    return len(queue._contents)

  # Just so we can print a queue
  def __str__(queue):
    #Just change bracket appearance to <---<
    return f"<{str(queue._contents)[1:-1]}<"
  def __repr__(queue):
    return str(queue)
###################################
# I WAS LAZY AND BROUGHT IN MY OLD ENQUEUE_ALL FUNCTION :P
def enqueue_all(q, x):
    """
    This function should take in a queue(q) and a list of values(x) and add the list of values into the queue. KEEP IN MIND
    that queues are FIFO (first in first out).
    :param q: A queue.
    :param x: A list of elements.
    :return: An updated queue.
    """
    for i in range(len(x)):
        Queue.enqueue(q, x[i])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def swap(q):
    """
    This function should take in a queue(q) and create a new queue where the first two elements have been swapped.
    YOU CAN ONLY USE ADT METHODS.
    :param q: A queue
    :return: A new queue with the first two elements swapped.
    """
    length = q.count()
    tempList = [None] * length
    for i in range(length):
        tempList[i] = q.dequeue()
    tempList[0], tempList[1] = tempList[1], tempList[0]
    outputQueue = Queue()
    enqueue_all(outputQueue, tempList)
    return outputQueue


# test code provided by me :))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
q1 = Queue()
enqueue_all(q1, [1, 2, 3])
print(f"{swap(q1)} and it should be\n<2, 1, 3<")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def same(q):
    """
    This function should take in a queue and give you a boolean about whether or not the first and last value in the queue
    are the same.
    YOU CAN ONLY USE ADT METHODS.
    :param q: A queue.
    :return: A boolean value.
    """
    length = q.count()
    tempList = [None] * length
    for i in range(length):
        tempList[i] = q.dequeue()
    if tempList[0] == tempList[-1]:
        return True
    else:
        return False


# test code provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
q2 = Queue()
enqueue_all(q2, [1 ,2, 3, 2, 3, 2, 1])
print(f"{same(q2)} and it should be True")
q3 = Queue()
enqueue_all(q3, [1, 2, 3, 4, 5, 3, 2, 2, 1, 2])
print(f"{same(q3)} and it should be False")