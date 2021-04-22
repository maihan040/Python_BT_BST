'''
	BT_Node.py

	Module to define the Binary Tree node class which will be used by the subsequent Binary Tree

    and Binary Search Tree class modules 

    This is the core element class whose instances will be used to build the trees

	Created: 02/23/2021

    Last Updated: 02/23/2021

	Verison: 1.0
'''

################################## Class Definition #####################################
#                                                                                       #
# Notes: Initially, nodes will have no children which is why the "left" and "right"     #
#       attributes are referring to "None"                                              #
#                                                                                       #
#       User should always pass a value for the new node to be created, but left and    #
#       right children fields are optional                                              #
#                                                                                       #
#########################################################################################

class Node:
    
    # define default values that will be used for each instance
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.right = right
        self.left = left
    
    # debug "__repr__" method to help out for debugging 
    def __repr__(self):
        return f"(Node val: {self.val}, Left child: {self.left}, Right child: {self.right})"
