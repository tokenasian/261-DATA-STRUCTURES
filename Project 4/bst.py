# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 5/16/2022
# Description: Implement the BST class by completing the provided skeleton code in the file bst.py. Once completed, your implementation will include the following methods:


from logging import root
import random
# from tkinter.font import names
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.
        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the BST tree is correct.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Method adds a new value to the tree. 
        Duplicate values are allowed. 
        If a node with that value is already in the tree, 
        the new value should be added to the right subtree of that node. 
        It must be implemented with O(N) runtime complexity.
        """
        #  from pseudocode from module

        parent = None
        n = self._root
        new_node = BSTNode(value) # create a new node

        while n != None:  # while n is not none
            parent = n  # parent < n
            if value < n.value: # is there a left child?
                n = n.left  #if so, parentoint the left child to n 
            else:  # is there a right child? 
                n = n.right  # if so, parentoint the right child to n
        # create a new node as the child of parent containing k, v
        if self.is_empty():  # is the tree emparentty?
            self._root = new_node  # if so, set the new node as the root
        elif value < parent.value:  # if the tree is not emparentty, then...
            parent.left = new_node 
        else:
            parent.right = new_node 

    def remove(self, value: object) -> bool:
        """
        This method removes a value from the tree. 
        The method returns True if the value is removed; 
        otherwise, it returns False. 
        It must be implemented with O(N) runtime complexity.

        """
        new_node = BSTNode(value)
        
        if self._root is None:
            return False

        curr = self._root
        parent = None

        while curr:
            if new_node.value < curr.value:  # is the target value smaller than the key value?
                parent = curr
                curr = curr.left  
            elif new_node.value > curr.value:  # is the target value larger than the key value?
                parent = curr
                curr = curr.right
            else:
                if curr.left is None and curr.right is None:
                    self.remove_no_subtrees(parent, curr)
                elif curr.left is None or curr.right is None:
                    self.remove_one_subtree(parent, curr)
                else:
                    self.remove_two_subtrees(parent, curr)
                return True
        return False

    def remove_no_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """Helper function for the remove method."""
        # case: node to be deleted has no children, aka the target is a leaf node.
        if node.left is None and node.right is None:
            if parent:  # is the node to be deleted not a root node?
                # set its parent left/right child to none
                if node == parent.left:
                    parent.left = None  # set to none
                else:
                    parent.right = None  # set to none
            else:  # is the tree only a root node?
                self._root = None  # if so, then set to node

    def remove_one_subtree(self, parent: BSTNode, node: BSTNode) -> None:
        """Helper function for the remove method."""
        # case: node to be deleted has only one child.
        # choose a child node.

        if node.left:
            child = node.left
        else:
            child = node.right

        # if the node to be deleted is not a root node, set parent to child
        if parent:
            if node == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:  # is the node to be deleted a root node?
            self._root = child  # set the root to child
        return root

    def remove_two_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """Helper function for the remove method."""
        
        temp = node        
        p = parent
        
        if node.right:  # if the right child is not None...
            succ = temp.right  # starting point, right subtree
            succParent = temp  # points to the prev node in BST
            
            while succ.left:  # locate leftmost node in a tree
                succParent = succ  # track the parent
                succ = succ.left  # go to the left to find the min value

            if node.right is not succ:
                succParent.left = succ.right
                succ.right = temp.right
            
            succ.left = temp.left  

            if p is None:  # base case
                self._root = succ
            elif p.value <= temp.value: # visit the right subtree
                p.right = succ
            else:  # visit the left subtree
                p.left = succ
        return

    def contains(self, value: object) -> bool:
        """
        Method returns True if the value is in the tree; otherwise, it returns False. 
        If the tree is empty, the method should return False. 
        It must be implemented with O(N) runtime complexity.
        """
        # from pseudocode from module
        node = self._root  # start at the root
        while node != None:  
            # examine if the current node is None, 
            # examine if the value is in the tree
            # examine if the search has failed
            if value == node.value:  # if node's value is equal, search is successful
                return True  # return success
            elif value < node.value:  # else if n < n.value...
                node = node.left  # n < n.left
            else:
                node = node.right  #n < n.right
        return False  # return failure if the search has failed

    def inorder_traversal(self) -> Queue:
        """
        Method will perform an inorder traversal of the tree, 
        return a Queue object that contains the values of the visited nodes,
        in the order they were visited. 
        If the tree is empty, the method returns an empty Queue. 
        It must be implemented with O(N) runtime complexity.
        """
        # from pseudocode from module
        q = Queue()  # new, empty queue
        def inOrder(node, ans):
            if not node:
                return
            inOrder(node.left, ans)
            ans.enqueue(node.value)  # process node
            inOrder(node.right, ans)
        inOrder(self._root, q)
        return q

    def find_min(self) -> object:
        """
        This method returns the lowest value in the tree. 
        If the tree is empty, the method should return None. 
        It must be implemented with O(N) runtime complexity.
        """
        if self.is_empty():  # is the BST empty?
            return None  # if so, return None
        current = self._root
        while current.left != None:  # loop to find the leftmost node
            current = current.left
        return current.value

    def find_max(self) -> object:
        """
        This method returns the highest value in the tree. 
        If the tree is empty, the method should return None. 
        It must be implemented with O(N) runtime complexity.
        """
        if self.is_empty():  # is the BST empty?
            return None  # if so, return None
        current = self._root
        while current.right != None:  # loop to find the rightmost node 
            current = current.right
        return current.value

    def is_empty(self) -> bool:
        """
        This method returns True if the tree is empty; otherwise, it returns False. 
        It must be implemented with O(1) runtime complexity.
        """
        return self._root is None

    def make_empty(self) -> None:
        """
        This method removes all of the nodes from the tree. 
        It must be implemented with O(1) runtime complexity.
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
