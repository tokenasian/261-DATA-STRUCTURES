# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 04/25/2022
# Description: Bag ADT assignment implemented with Dynamic Array


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag. 
        """
        self._da.append(value)  # O(1) complexity

    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag, that matches the provided value object. 
        """
        # O(n) complexity 
        for ele in range(self._da.length()):

            if self._da[ele] == value:
                self._da.remove_at_index(ele)  # checks for matches to be removed
                return True  #returns true if some object was actually removed from the bag. 
        return False  # returns false if no matches are found

    def count(self, value: object) -> int:
        """
        Returns the number of elements in the bag, that match the provided value object. 
        """
        count = 0
        # O(n) complexity 
        for ele in range(self._da.length()):
            if self._da[ele] == value:
                count += 1  # increments the number of elements
        return count

    def clear(self) -> None:
        """
        Clears the contents of the bag. 
        """
        self._da = DynamicArray()  # O(1) complexity 

    def equal(self, second_bag: "Bag") -> bool:
        """
        Checks if the contents of the original bag and secod_bag are both equal.
        Return True when bags are equal,
        Return False otherwise. 
        """
        if self.size() != second_bag.size():  # compare the bag lengths
            return False

        else: 
            for item in range(self.size()):
                idx = self._da.get_at_index(item)
                if self.count(idx) != second_bag.count(idx):
                    return False 
        return True

    def __iter__(self):
        """
        Enables the Bag to iterate across itself.
        """
        self.index = 0
        return self

    def __next__(self):
        """
        Returns the next item in the Bag, based on the current location of the iterator. 
        """
        try:
            value = self._da[self.index]
        except DynamicArrayException:
            raise StopIteration

        self.index = self.index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
