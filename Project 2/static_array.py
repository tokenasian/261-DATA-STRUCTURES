# Course:       CS261 - Data Structures
# Description:  Data structure for assignments


class StaticArrayException(Exception):
    """
    Custom exception for Static Array class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class StaticArray:
    """
    Implementation of Static Array Data Structure
    Implemented methods: get(), set(), length()

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self, size=10) -> None:
        """
        Create array of given size
        Initialize all elements with values of None
        If requested size is not a positive number, raise StaticArray Exception
        """
        if size < 1:
            raise StaticArrayException('Array size must be a positive integer')

        # The underscore denotes this as a private variable and
        # private variables should not be accessed directly.
        # Use the length() method to get the size of a StaticArray.
        self._size = size

        # Remember, this is a built-in list and is used here
        # because Python doesn't have a fixed-size array type.
        # Don't initialize variables like this in your assignments!
        self._data = [None] * size

    def __iter__(self) -> None:
        """
        Disable iterator capability for StaticArray class
        This means loops and aggregate functions like
        those shown below won't work:

        arr = StaticArray()
        for value in arr:     # will not work
        min(arr)              # will not work
        max(arr)              # will not work
        sort(arr)             # will not work
        """
        return None

    def __str__(self) -> str:
        """
        Return content of static array in human-readable form
        """
        out = "STAT_ARR Size: "
        out += str(self._size)
        out += " " + str(self._data)
        return out

    def get(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises StaticArrayException
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        return self._data[index]

    def set(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises StaticArrayException
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        self._data[index] = value

    def __getitem__(self, index: int):
        """
        Same functionality as get() method above, but called differently
        These snippets of code are equivalent:

        arr = StaticArray()
        arr.set(0, 'hello')
        print(arr.get(0))

        arr = StaticArray()
        arr[0] = 'hello'
        print(arr[0])
        """
        return self.get(index)

    def __setitem__(self, index: int, value: object) -> None:
        """
        Same functionality as set() method above, but called differently
        These snippets of code are equivalent:

        arr = StaticArray()
        arr.set(0, 'hello')
        print(arr.get(0))

        arr = StaticArray()
        arr[0] = 'hello'
        print(arr[0])
        """
        self.set(index, value)

    def length(self) -> int:
        """Return length of the array (number of elements)."""
        return self._size

    def size(self):
        pass


if __name__ == "__main__":

    # Using the Static Array #

    # create a new StaticArray object to store 5 elements
    arr = StaticArray(5)

    # set the value of each element equal to its index multiplied by 10
    for index in range(5):
        arr[index] = index * 10

    # print the values of all elements in reverse order
    for index in range(4, -1, -1):
        print(arr[index])

    # print the number of elements stored in the array
    print(arr.length())

    # Special consideration below #

    # Don't do this! This creates a built-in Python list and if you use
    # one you'll lose points.
    forbidden_list = [None] * 10
