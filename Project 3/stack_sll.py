# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: May 2nd
# Description: Implement a Stack ADT class.


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack. 
        O(1) runtime complexity.
        """
        if self.is_empty():  # is the stack empty? 
            self._head = SLNode(value)  # if so, create a new head 

        else:  # create a link for the new node to the head
            new_node = SLNode(value, self._head)  
            new_node.next = self._head  # set next of new node as head
            self._head = new_node  # update the head to point to the new node

    def pop(self) -> object:
        """
        Removes the top element from the stack, returns its value. 
        O(1) runtime complexity. 
        """
        if self.is_empty():  # is the stack empty? 
            raise StackException  # if so, raise exception

        else: 
            popped_node = self._head.value  # remove the top element before the node is deleted
            self._head = self._head.next  # save the preceding value as the new head
            return popped_node

    def top(self) -> object:
        """
        Returns the value of the top element of the stack without removing it. 
        O(1) runtime complexity.
        """
        if self.is_empty():  # is the stack empty?
            raise StackException()  # if so, raise exception
        else:  # return the value of top element, without removing it
            return self._head.value  

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
