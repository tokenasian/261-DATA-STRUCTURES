# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 5/16/2022
# Description: Implement the AVL class (a subclass of BST) by completing the provided skeleton code in the file avl.py.


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """This method adds a new value to the tree while maintaining its AVL property. 
        Duplicate values are not allowed. 
        If the value is already in the tree, the method should not change the tree. 
        O(log N) runtime complexity."""
        node = AVLNode(value)
        if self.is_empty(): # is the root empty?
            self._root = node  # if the root is empty, return node as the root
        else: 
            curr = self._root  # curr as root
            while curr is not None:
                if value < curr.value:  # if value is less than current node, recur for left subtree.
                    if curr.left is None:  # if the left sub tree has no value...
                        curr.left = node
                        node.parent = curr
                        break  # terminate the loop
                    else:
                        curr = curr.left  # set the left child to curr
                elif value > curr.value:  # if value is greater than current node, recur for right subtree.
                    if curr.right is None:  # if the right sub tree has no value...
                        curr.right = node
                        node.parent = curr
                        break  # terminate the loop
                    else:
                        curr = curr.right
                else:  # if the key is not found in the tree
                    return
            while node is not None:  # rebalance
                self.rebalance(node)
                node = node.parent

    def remove(self, value: object) -> bool:
        """
        This method should remove the value from the AVL tree. 
        The method returns True if the value is removed from the AVL Tree; 
        otherwise, it returns False. 
        It must be implemented with O(log N) runtime complexity.
        """
        p = self.remove_rec(value)
        
        if p == False:
            return False

        # pseudocode
        while p != None:  # rebalancing act
            self.rebalance(p)
            p = p.parent
        return True
        
    def balance_factor(self, node: AVLNode) -> int:
        """
        Helper function that returns the balance factor of a given node,
        by subtracting the right height from the left.
        """
        # use to determine whether or not the subtree rooted at that node is height-balanced. 
        # balance factor of a node N is the difference in height 
        # between N’s right subtree and its left subtree:
        # balanceFactor(N) = height(N.right) - height(N.left)
        return self.get_height(node.right) - self.get_height(node.left)

    def get_height(self, node: AVLNode) -> int:
        """
        Helper function that returns the root height to a given node. 
        Is the node None? If the node is None, then return -1.
        Is the node not none? If the node is not None, then return the node height.
        """
        if node is None:  # is node none?
            return -1  # return - 1
        else:  # return the height if node is not none
            return node.height

    def rotate_left(self, node: AVLNode) -> AVLNode:
        """
        Helper method that rotates left around the node.
        """
        # from pseudocode from module
        # height = an integer representing the height of the node
        # left = the left child node
        # right = the right child node
        # parent = the parent node

        c = node.right
        node.right = c.left

        if node.right != None: 
            node.right.parent = node

        c.left = node
        node.parent = c

        self.update_height(node)
        self.update_height(c)
        
        return c

    def rotate_right(self, node: AVLNode) -> AVLNode:
        """
        Helper method that rotates right around the node.
        """
        # from pseudocode from module
        # height = an integer representing the height of the node
        # left = the left child node
        # right = the right child node
        # parent = the parent node

        c = node.left  
        node.left = c.right  

        if node.left != None:
            node.left.parent = node

        c.right = node
        node.parent = c

        self.update_height(node)
        self.update_height(c)
        return c

    def update_height(self, node: AVLNode) -> None:
        """
        Helper method that updates the height of a given node.
        """

        if node.right != None:
            node.height = self.get_height(node.left)
        else:
            node.height = - 1
        if node.left != None:
            node.height = self.get_height(node.right)
        else:
            node.height = -1
        
        # from pseudocode from module
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def rebalance(self, node: AVLNode) -> None:
        """
        Helper method that rebalances the node.
        """
        # from pseudocode from module
        
        if self.balance_factor(node) < -1: 
            # L to R
            if self.balance_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
                node.left.parent = node
            # L to L
            newNodeParent = node.parent
            newSubtreeRoot = self.rotate_right(node)
            newSubtreeRoot.parent = newNodeParent
            
            if not newNodeParent:
                self._root = newSubtreeRoot
                newSubtreeRoot.parent = None
                return
            
            elif newNodeParent.left == node:
                newNodeParent.left = newSubtreeRoot
            else:
                newNodeParent.right = newSubtreeRoot

        elif self.balance_factor(node) > 1:
            # R to L 
            if self.balance_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)  # update the pointers
                node.right.parent = node
            # R to R
            newNodeParent = node.parent
            newSubtreeRoot = self.rotate_left(node)
            newSubtreeRoot.parent = newNodeParent
            
            if not newNodeParent:
                self._root = newSubtreeRoot
                newSubtreeRoot.parent = None
                return
            
            if newNodeParent.left == node:
                newNodeParent.left = newSubtreeRoot
            else:
                newNodeParent.right = newSubtreeRoot

        else:
            self.update_height(node)

    def remove_rec(self, value) -> bool:
        """
        Helper function for remove method.
        """
        if self._root is None:
            return False

        node = self._root
        parent = None  

        while node:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                break        
        if node is None:
            return False      

        if parent is None:
            if self._root.left is None and self._root.right is None:  
                self._root = None
                return
            elif self._root.left is None:  
                self._root = self._root.right 
            elif self._root.right is None:
                self._root = self._root.left
                
            else:  # node to be deleted has two children
                # find successor
                succ = None
                succParent = None
                if node.right:  # if node.right is not None...
                    succ = node.right # starting point, right subtree
                if succ:  # if succ is not None...
                    while succ.left: # loop to find succ and parent
                        succParent = succ  # track the parent
                        succ = succ.left  # go to the left to find the min value
                # delete successor
                if succParent:  # if succ Parent is not None...
                    # check if the parent of the in order succ is the root, or not
                    node.value = succ.value
                    succParent.left = succ.right  # make left equal to in order succ's right
                    return succParent               
                else:  # if there is no successor, then assign
                    node.value = succ.value
                    node.right = succ.right                                        
                    if node.right:
                        return node.right
                    else:
                        return node.left
            return parent
        # leaf node case
        if node.left is None and node.right is None:
            if parent: 
                if node is parent.left:
                    parent.left = None
                else:
                    parent.right = None
            return parent         
        # special case detected
        if node.left is None:
            if node == parent.left:
                parent.left = node.right
            else:
                parent.right = node.right
            return parent
        if node.right is None:
            if node == parent.left:
                parent.left = node.left
            else:
                parent.right = node.left
            return parent
        else: 
            succ = node.right
            succParent = None
            while succ.left:  # while successor.left is not none...
                succParent = succ
                succ = succ.left
            if succParent:  # if successor parent is not none...
                node.value = succ.value
                succParent.left = succ.right
                return succParent
            elif parent.value <= node.value:
                parent.right = succ
                succ.left = node.left
                node.left.parent = succ
                succ.parent = parent
                return succ
            else:
                parent.left = succ
                succ.left = node.left
                node.left.parent = succ
                succ.parent = parent
                return succ
        
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
