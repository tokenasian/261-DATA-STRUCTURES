# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: May 2nd
# Description: Implement a Singly LinkedList data structure.


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list.
        """

        new_node = SLNode(value) # create new node
        new_node.next = self._head.next
        self._head.next = new_node  # replace with the new node

    def insert_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list.
        """
        new_node = SLNode(value)

        if self._head is None:
            self._head = new_node
            return
        
        end_node = self._head
        while (end_node.next) is not None:
            end_node = end_node.next
        end_node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new value at the specified index position in the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        """
        if index < 0 or index > self.length():  # is the index out of range?
            raise SLLException  # if so, raise exception

        count = 0  # initialize count
        previous_node = self._head  # initialize pointer

        while count != index:  # traverse through the list, locate the specified index position 
            previous_node = previous_node.next
            count += 1  # increment the count by 1

        new_node = SLNode(value)  # insert the new node
        new_node.next = previous_node.next  # update the pointers
        previous_node.next = new_node  

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node at the specified index position from the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        """
        if index < 0 or index >= self.length():  # is the index out of range?
            raise SLLException  # if so, raise exception
        
        # initialize the count
        count = 0
        current = self._head  
        
        while count != index:  # traverse through the list, locate the target node at the given index
            current = current.next
            count += 1  # increment the count by 1

        new_node = current.next.next  # update the pointers
        current.next = new_node  

    def remove(self, value: object) -> bool:
        """
        Traverses the list from the beginning to the end
        Removes the first node that matches the provided “value” object. 
        """
        node = self._head 
        while node.next is not None:  # traverse through the list, find the node that matches the passed object
            if value == node.next.value:  # remove the first node matching provided “value” object
                node.next = node.next.next
                return True 
            else: 
                node = node.next
        return False  # no matching node value found upon reaching the tail

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value” object. 
        The method then returns this number.
        """
        count = 0  # initialize the count
        current = self._head.next

        while current is not None:  # traverse through the list until we reach the end
            if value == current.value:  # locate the matching target value
                count += 1  # increment the count by 1
            current = current.next
        return count  # return the count 

    def find(self, value: object) -> bool:
        """
        Returns a Boolean value based on whether or not the provided “value” object exists in the list.
        """
        current = self._head

        while current.next is not None:  # traverse through the list
            if value == current.next.value:  # locate the value object in the list
                return True  
            current = current.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Returns a new LinkedList object that contains,
        the requested number of nodes from the original list, 
        starting with the node located at the requested start index. 
        If the original list contains N nodes, 
        a valid start_index is in range [0, N - 1] inclusive. 
        The original list cannot be modified. 
        The runtime complexity of your implementation must be O(N).
        """
        if (start_index < 0) or (size < 0) or (start_index + size > self.length()) or (start_index >= self.length()):
            raise SLLException

        current = self._head
        newLL = LinkedList()
        
        while start_index != 0:
            current = current.next
            start_index -= 1

        while size > 0:
            current = current.next
            newLL.insert_back(current.value)
            size -= 1
        return newLL

if __name__ == '__main__':

    print('\n# insert_front example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_front('A')
    lst.insert_front('B')
    lst.insert_front('C')
    print(lst)

    print('\n# insert_back example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_back('C')
    lst.insert_back('B')
    lst.insert_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_at_index example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# remove example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# remove example 2')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")
