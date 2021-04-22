'''
        BT_Class_Driver.py

        Module to fully test the BT class  

	Created: 02/23/2021

        Last Updated: 02/25/2021

	Verison: 1.0
        
        Requires: "BT.py" module

'''

######################################### Imports ###############################################
#												#
# BT.py: Needed to create a binary tree and use the subsequent methods				#
# BST.py: Needed to create a binary tree and use the subsequent methods				#
# BT_Functions: Needed to generate random int values used to popluate the tree, and the         #
#               function decorators                                                             #
#												#
#################################################################################################
from BT import BT
from BST import BST
import BT_Functions as functions

######################################## Functions ##############################################
#												#
# Below are the functions used to fully test the given tree class and its methods		#
#												#
#################################################################################################

#
# Getter test functions
#
@functions.getter_method_decorator
def test_get_pre_order_traversal(tree):
        # get the order
        pre_order = tree.get_pre_order_traversal()

        # print the order 
        for i in pre_order: 
                print(str(i), end = ' ')
        
        # add new line
        print()

@functions.getter_method_decorator  
def test_get_in_order_traversal(tree):

        # get the order
        in_order = tree.get_in_order_traversal()

        # print the order 
        for i in in_order: 
                print(str(i), end = ' ')
        
         # add new line
        print()

@functions.getter_method_decorator 
def test_get_post_order_traversal(tree):
        # get the order
        in_order = tree.get_post_order_traversal()

        # print the order 
        for i in in_order: 
                print(str(i), end = ' ')
        
         # add new line
        print()

@functions.getter_method_decorator 
def test_get_level_order_traversal(tree):
        # get the order
        in_order = tree.get_level_order_traversal()

        # print the order 
        for i in in_order: 
                print(str(i), end = ' ')
        
         # add new line
        print()

@functions.getter_method_decorator
def test_get_min_level_sum(tree):
        # function to test the get level sum function 

        # get the min level sum
        min_sum = tree.get_min_level_sum()
        print(str(min_sum))

#
# Modifying test functions
#
@functions.modifier_methods_decorator
def test_populate_tree(tree):

        # function used for this module to populate the tree with values so that 
        # the methods from the given tree class can be tested 

        # local variables 
        numbers_to_insert = functions.generate_values()

        # add each number to the tree
        for n in numbers_to_insert:
                tree.insert_node(n)

@functions.modifier_methods_decorator
def test_delete_tree(tree):
        # function to test the delete function

        # delete the tree
        tree.delete_tree()

@functions.modifier_methods_decorator
def test_filter(tree, k):
        # function to test the filter function 

        # filter the tree
        tree.filter_tree(k)

@functions.modifier_methods_decorator
def test_balance_tree(tree):
        # function to test the balance function

        # balance the tree and return the new tree
        # that was created
        return tree.balance_bst()

@functions.modifier_methods_decorator
def test_sorted_arr_to_bst(tree, *args):
        # function which tests building a BST 
        # when passed a sorted list 
        return tree.sorted_arr_to_bst(args)

@functions.modifier_methods_decorator
def test_merge_trees(tree1, tree2):
        # function which builds a consolidated binary search tree
        # from two two existing binary search trees
        merged_tree = tree1.merge_trees(tree2)
        return merged_tree

#
# Function to completely test a tree
#
def fully_test_tree(tree, *args):

        # populate the tree 
        #test_populate_tree(tree)

        # call function to test the pre order traversal 
        #test_get_pre_order_traversal(tree)

        # call function to test the in order traversal 
        #test_get_in_order_traversal(tree)

        # call function to test the post order traversal 
        #test_get_post_order_traversal(tree)

        # call function to test the level order traversal 
        #test_get_level_order_traversal(tree)

        # call to test the get min level sum function 
        #test_get_min_level_sum(tree)

        # call to test the filter function 
        #test_filter(tree, 1)

        # call to test the delete function
        #test_delete_tree(tree)

        #########################################################
        # Below functions only apply to Binary search trees     #
        #########################################################
        
        if not args: 

                if isinstance(tree, BST):
                        #test_balance_tree(tree)
                        pass
        else:

                if isinstance(tree, BST): 
                        return test_merge_trees(tree, args[0])
                        pass
                
                if isinstance(tree, BST): 
                        #return test_sorted_arr_to_bst(tree, args[0])
                        pass

        


########################################### Main ################################################
#												#
# Calls all the individual test functions to fully test the BT class            		#
#												#
#################################################################################################

#
# create binary tree/s and test the functionalities
#

# Local variables
my_bt = BT()
my_bst = BST()
pd_bt = BT() # pdt = pre_defined_tree
pd_bst = BST()
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# used specifically to test the filter function, to ensure the leaf/parent contains the
# target nodes that need to be removed 

# bin_tree
pd_bt.insert_node(5)
pd_bt.insert_node(2)
pd_bt.insert_node(1)
pd_bt.insert_node(2)
pd_bt.insert_node(2)
pd_bt.insert_node(3)
pd_bt.insert_node(8)

# bin_search_tree
pd_bst.insert_node(9)
pd_bst.insert_node(8)
pd_bst.insert_node(7)
pd_bst.insert_node(6)
pd_bst.insert_node(5)
pd_bst.insert_node(4)
pd_bst.insert_node(3)
pd_bst.insert_node(2)
pd_bst.insert_node(1)

# bin_search_tree instances to check the merge functionality 
pd_bst1 = BST()
pd_bst1.insert_node(3)
pd_bst1.insert_node(2)
pd_bst1.insert_node(1)
pd_bst1.insert_node(4)
pd_bst1.insert_node(5)

pd_bst2 = BST()
pd_bst2.insert_node(8)
pd_bst2.insert_node(7)
pd_bst2.insert_node(6)
pd_bst2.insert_node(9)


#
# call the test function to test a given tree
#

# call "fully_test_tree" function to test the binary tree
#fully_test_tree(my_bt)

# call "fully_test_tree" function to test the binary search tree
#fully_test_tree(pd_bst)

# call "fully_test_tree" function to test the binary search tree
# function which builds a complete BST from a sorted list 
#fully_test_tree(BST(), sorted_arr)

# call "fully_test_tree" function to test the merging of two
# bst instances and obtain the final tree 
merged_tree = fully_test_tree(pd_bst1, pd_bst2)
print("Done merging")