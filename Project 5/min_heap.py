# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 5/23/2022
# Description: Implement the MinHeap class by completing the provided skeleton code in the file min_heap.py.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining heap property.
        O(log N).
        """
        self._heap.append(node)  # if the heap has a value, add node object to the end of the heap,
        index = self._heap.length() - 1  # then define the index
        parent_idx = index

        while parent_idx != 0:
            parent_idx = (parent_idx - 1) // 2  # computing the inserted element's parent index, i - 1 / 2

            if self._heap.get_at_index(parent_idx) > self._heap.get_at_index(
                    index):  # compare the value of the inserted element with the value of its parent
                self.swap(index,
                          parent_idx)  # swap the elements, do not repeat if the element has reached the beginning of the array
                index = parent_idx

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty;
        otherwise, it returns False.
        O(1).
        """
        return self._heap.is_empty()

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        O(1).
        """
        if self.is_empty() == True:  # is the heap empty?
            raise MinHeapException()  # if so, raise exception
        return self._heap.get_at_index(0)  # return the value of the first element (the root) in the array

    def remove_min(self) -> object:
        """Returns an object with the minimum key, removes it from the heap. If the heap is empty, the method raises a MinHeapException.
        For the downward percolation of the replacement node:
        if both children of the node have the same value (and are both smaller than the node), swap with the left child.
        O(log N)."""
        if self._heap.is_empty():  # is the heap empty?
            raise MinHeapException  # if so, raise exception

        min_value = self.get_min()  # define the min value
        prev_index = self._heap.length() - 1
        parent_index = self._heap.get_at_index(prev_index)
        self._heap.set_at_index(0, parent_index)  # swap the values
        self._heap.remove_at_index(prev_index)  # remove the last value
        percolate_down(self._heap, 0)  # percolate down...
        return min_value  # return the min value

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a Dynamic Array with objects in any order, and builds a proper MinHeap from them.
        The current content of the MinHeap is overwritten.
        Must be O(N), not O(N log N),
        """
        new_heap = DynamicArray()  # copy the dynamic array, replace the heap
        for i in range(da.length()):
            value = da.get_at_index(i)
            new_heap.append(value)
        self._heap = new_heap  # make the new_heap our current heap

        parent_index = (da.length() // 2) - 1
        while (parent_index != -1):
            percolate_down(self._heap, parent_index)  # percolate down...
            parent_index -= 1  # increment

    def size(self) -> int:
        """
        Returns the number of items currently stored in the heap.
        O(1).
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        This method clears the contents of the heap.
        O(1).
        """
        self._heap = DynamicArray()
        return

    def swap(self, first_index, second_index):
        """
        Helper function to swap two indices in a list
        """
        temp = self._heap[first_index]
        self._heap[first_index] = self._heap[second_index]
        self._heap[second_index] = temp


def percolate_down(da: DynamicArray, index):
    """Helper function"""
    left_child = index * 2 + 1  # define the left child of node at index
    right_child = index * 2 + 2  # define the right child of node at index
    size = da.length() - 1  # define the length
    min_value = index  # min_value value node at index
    # compare the left and right child to find the min_value value
    if left_child <= size and da.get_at_index(min_value) > da.get_at_index(left_child):
        min_value = left_child
    if right_child <= size and da.get_at_index(min_value) > da.get_at_index(right_child):
        min_value = right_child
    if min_value != index:
        da.swap(index, min_value)  # swap with a child having a smaller value
        percolate_down(da, min_value)  # percolate down...

def heapsort(da: DynamicArray) -> None:
    """
    Function receives a DynamicArray, sorts in non-ascending order,
    using the Heapsort algorithm.
    Must sort the array in place, without creating a new array.
    Must be O(N log N).
    """

    n = da.length()
    k = n - 1
    heap = MinHeap()
    heap.build_heap(da)
    while k >= 0:
        da[k] = heap.remove_min()
        k -= 1


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)