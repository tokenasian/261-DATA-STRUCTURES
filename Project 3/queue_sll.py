# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: May 2nd
# Description: Implement a Queue ADT class.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue. 
        O(1)runtime complexity.
        """
        new_node = SLNode(value)
        
        if self.is_empty():  # is the queue empty?
            self._head = self._tail = new_node  # if so, create new head
        
        else: 
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        """
        Removes and returns the value from the beginning of the queue. 
        O(1)runtime complexity.
        """
        if self.is_empty():  # is the queue empty?
            raise QueueException  # if so, raise exeption

        else:
            target_val = self._head  # save the value
            self._head = target_val.next  # remove the value from the beginning of the queue
            return target_val.value  # return value

    def front(self) -> object:
        """
        Returns the value of the front element of the queue,
        without removing it. 
        O(1) runtime complexity.
        """
        if self.is_empty():  # is the queue empty?
            raise QueueException()  # if so, raise exception

        else:  # return the value of the front element of the queue
            front_element = self._head.value
            return front_element

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
