"""
Test for BinaryTree class
"""

import unittest

from binarytree.node import Node
from binarytree.binarytree import BinaryTree


class BinaryTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Binary Tree
    """

    def test_add_nodes_from_list(self):
        """
            (positive testing of add function)
        Create a binary tree.
        Add nodes from list to the binary tree.
        Test that all the nodes are placed correctly
        """
        binary_tree = BinaryTree(4)
        nodes = [Node(3), Node(1), Node(2), Node(6), Node(7), Node(5)]
        for node in nodes:
            binary_tree.add(node)
        self.assertEqual(binary_tree.root.value, 4)
        self.assertEqual(binary_tree.root.left.value, 3)
        self.assertEqual(binary_tree.root.right.value, 6)

    def test_call_add_non_integers_raised_error(self):
        """
            (negative testing of add function)
        Create a binary tree.
        Test that call of add method with incorrect input values raises Value error
        """
        binary_tree = BinaryTree(4)
        not_nodes = [4, 10.44465, 'two', None, {}, ['wow']]
        for val in not_nodes:
            self.assertRaises(ValueError, binary_tree.add, val)

    def test_add_to_empty_binary_tree(self):
        """
            (end-to-end testing of add function)
        Create an empty binary tree.
        Add nodes from a values generator to the binary tree.
        Test that all the nodes are placed correctly
        """
        binary_tree = BinaryTree()
        for val in range(1, 5):
            binary_tree.add(Node(val))
        self.assertEqual(binary_tree.root.value, 1)
        self.assertEqual(binary_tree.root.right.value, 2)
        self.assertEqual(binary_tree.root.right.right.value, 3)
        self.assertEqual(binary_tree.root.right.right.right.value, 4)

    def test_find_existing_nodes(self):
        """
            (positive testing of find function)
        Create an empty binary tree.
        Add nodes from list to the binary tree.
        Test that the nodes of the binary tree can be found
        """
        binary_tree = BinaryTree()
        node_values = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values:
            binary_tree.add(Node(val))
        for val in node_values:
            self.assertEqual(binary_tree.find(Node(val)).value, Node(val).value)

    def test_call_find_incorrect_values(self):
        """
            (negative testing of find function)
        Create an empty binary tree.
        Add nodes from list to the binary tree.
        Test that call of find with incorrect values returns None
        """
        binary_tree = BinaryTree()
        node_values = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values:
            binary_tree.add(Node(val))
        wrong_values = [Node(0), Node(1), 10, 2, 13, 100, 548150, 10.44465, 'two', None, {}]
        for val in wrong_values:
            self.assertEqual(binary_tree.find(val), None)

    def test_find_odd_numbers_in_even_number_binary_tree(self):
        """
            (end-to-end testing of find function)
        Create an empty binary tree.
        Add nodes with even numbers from generator to the binary tree.
        Test that call of find with odd numbers from generator returns None
        """
        binary_tree = BinaryTree()
        for val in range(10, 0, -1):
            if not val % 2:
                binary_tree.add(Node(val))
        for val in range(10, 0, -2):
            self.assertEqual(binary_tree.find(Node(val)).value, Node(val).value)
        for val in range(10, 0, -1):
            if val % 2:
                self.assertEqual(binary_tree.find(Node(val)), None)

    def test_remove_existing_nodes(self):
        """
            (positive testing of remove function)
        Create a binary tree by adding nodes from list.
        Remove nodes using the values from the list.
        Test that the nodes of the binary tree are removed correctly
        """
        binary_tree = BinaryTree()
        node_values = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values:
            binary_tree.add(Node(val))
        while node_values:
            self.assertEqual(binary_tree.remove(Node(node_values[-1])).value, node_values[-1])
            node_values.pop()
        self.assertEqual(binary_tree.root.value, None)

    def test_call_remove_incorrect_values(self):
        """
            (negative testing of remove function)
        Create an empty binary tree.
        Add nodes from list of values to the binary tree.
        Test that call of remove with incorrect values returns None
        """
        binary_tree = BinaryTree()
        node_values = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values:
            binary_tree.add(Node(val))
        wrong_values = [Node(0), Node(100), 10, 5, 100, 548150, 10.44465, None, 'two', {}]
        for val in wrong_values:
            self.assertEqual(binary_tree.remove(val), None)

    def test_call_remove_already_removed_nodes(self):
        """
            (end-to-end testing of remove function)
        Create an empty binary tree.
        Add nodes from list of values to the binary tree and remove them.
        Test that call of remove with already removed nodes returns None
        """
        binary_tree = BinaryTree()
        node_values = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values:
            binary_tree.add(Node(val))
        self.assertEqual(binary_tree.remove(Node(node_values[0])).value, node_values[0])
        while node_values:
            self.assertEqual(binary_tree.remove(Node(node_values[-1])), None)
            node_values.pop()

    def test_get_height_of_binary_trees(self):
        """
            (positive testing of get_height function)
        Create binary trees with different number and sequence of nodes.
        Test that their height is calculated correctly
        """
        binary_tree_1 = BinaryTree(5)
        self.assertEqual(binary_tree_1.get_height(), 0)

        binary_tree_2 = BinaryTree()
        node_values_2 = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values_2:
            binary_tree_2.add(Node(val))
        self.assertEqual(binary_tree_2.get_height(), 3)

        binary_tree_3 = BinaryTree()
        node_values_3 = [14, 7, 12, 11, 10, 6, 9]
        for val in node_values_3:
            binary_tree_3.add(Node(val))
        self.assertEqual(binary_tree_3.get_height(), 5)

    def test_call_get_height_of_empty_tree(self):
        """
            (negative testing of get_height function)
        Create an empty binary tree and a binary tree with non-integer root value.
        Test that call of get_height method of created binary trees returns None
        """
        binary_tree_1 = BinaryTree()
        binary_tree_2 = BinaryTree('non-integer')
        self.assertEqual(binary_tree_1.get_height(), None)
        self.assertEqual(binary_tree_2.get_height(), None)

    def test_binary_tree_from_generator_and_get_height(self):
        """
            (end-to-end testing of get_height function)
        Create a binary tree with a root.
        Add nodes from generator to the binary tree.
        Test that the height of the binary tree is equal to the generator length
        """
        binary_tree = BinaryTree(0)
        for val in range(1, 50):
            binary_tree.add(Node(val))
        self.assertEqual(binary_tree.get_height(), len(range(1, 50)))

    def test_get_dfs_of_binary_trees(self):
        """
            (positive testing of get_dfs function)
        Create binary trees with different node values and sequence.
        Test that their DFS is traversed correctly
        """
        binary_tree_1 = BinaryTree()
        node_values_1 = [6, 5, 11, 12, 2, 7]
        dfs_1 = [6, 5, 2, 11, 7, 12]
        for val in node_values_1:
            binary_tree_1.add(Node(val))
        binary_tree_1.get_dfs()
        self.assertEqual(binary_tree_1.dfs_nodes, dfs_1)

        binary_tree_2 = BinaryTree()
        node_values_2 = [14, 7, 12, 11, 10, 6]
        dfs_2 = [14, 7, 6, 12, 11, 10]
        for val in node_values_2:
            binary_tree_2.add(Node(val))
        binary_tree_2.get_dfs()
        self.assertEqual(binary_tree_2.dfs_nodes, dfs_2)

    def test_get_dfs_empty_tree(self):
        """
            (negative testing of get_dfs function)
        Create an empty binary tree.
        Test that the DFS traversal cannot be implemented
        """
        binary_tree = BinaryTree()
        binary_tree.get_dfs()
        self.assertFalse(binary_tree.dfs_nodes)

    def test_get_dfs_3(self):
        """
            (end-to-end testing of get_dfs function)
        Create an empty binary tree.
        Add the root node to the binary tree.
        Add other nodes to the binary tree.
        Test that the DFS is traversed correctly on different stages
        """
        binary_tree = BinaryTree()
        root_value = [15]
        node_values = [14, 13, 17, 25, 8]
        dfs = [15, 14, 13, 8, 17, 25]

        binary_tree.add(Node(root_value[0]))
        binary_tree.get_dfs()
        self.assertEqual(binary_tree.dfs_nodes, root_value)

        for val in node_values:
            binary_tree.add(Node(val))
        binary_tree.get_dfs()
        self.assertEqual(binary_tree.dfs_nodes, dfs)

        binary_tree.add(Node(30))
        dfs.append(30)
        binary_tree.get_dfs()
        self.assertEqual(binary_tree.dfs_nodes, dfs)
