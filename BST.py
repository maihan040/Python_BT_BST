'''
	BST.py

	Module to define the "Binary Search Tree" class. This class is being derived from the "BT" class

	and will inherit all the functions that can be applied to the BST in addition to creating newly

	defined ones

	Created: 02/24/2021

	Last Updated: 02/25/2021

	Verison: 1.0
'''

#################################### Class Definition ###########################################
#                                                                                       	#
# Note: Tree will initially contain an empty Node object, unless the user specifies a value	#
#                                                                                       	#
#       Should the user not supply a data value for the root of the tree, then the value will  	#
#	default (to None) in the init method							#
#												#
#	Binary search trees contain a strict ordering, namely that the left child is always	#
#	smaller than then parent, and the right child being greater/equal to the parent.	#
#	This ordering will be followed in the "insert" method					#
#                                                                                       	#
#################################################################################################

#################################### Methods defined ############################################
#                                               						#
# Following methods are inherited/defined inside the class definition:                          #
#												#
#	//GETTER METHODS//									#
#	get_pre_order_traversal	- inherited from parent class					#
# 	get_in_order_traversal - inherited from parent class					#
# 	get_post_order_traversal - inherited from parent class					#
#	get_level_order_traversal - inherited from parent class					#
#	get_tree_height	- inherited from parent class						#
#	get_min_max - OVERIDDEN IN THIS CLASS							#
#	get_min_level_sum - inhertied from parent class -CHECK THIS METHOD 			#
# 	get_floor_ceil - NEW FUNCTIONALITY SPECIFIC TO THIS CLASS				#
# 												#
#	//MODIFYING METHODS//									#
#	filter_tree 										#
#	delete_tree 										#											#
#   	insert__node - OVERIDDEN IN THIS CLASS                         				#
#	invert__bin_tree - OVERIDDEN, as it doesn't apply to a BST due to its strict ordering	#
#	balance_tree - NEW FUNCTIONALIRTY SPECIFIC TO THIS CLASS				#
# 	sorted_arr_to_bst - NEW FUNCTIONALITY SPECIFIC TO THIS CLASS				#
#												#
#	//BST operations//									#
#	merge_trees - NEW FUNCTIONALITY SPECIFIC TO THIS CLASS					#	
# 												#
#################################################################################################

######################################### Imports ###############################################
#												#
# BT class from the BT module									#
# Node.py: Node used to build the the individual nodes of the binary tree                     	#
#												#
#################################################################################################
from BT import BT as BT_Class
import Node
from queue import Queue

class BST(BT_Class):
                                           						 										
	def __init__(self, val = None):
		# inherit all the methods from the parent 
		super().__init__(val)
	
	####################### parent's methods #############################
	def get_pre_order_traversal(self):
		return super().get_pre_order_traversal()
	
	def get_in_order_traversal(self):
		return super().get_in_order_traversal()
	
	def get_post_order_traversal(self):
		return super().get_post_order_traversal()
	
	def get_level_order_traversal(self):
		return super().get_level_order_traversal()
	
	def get_tree_height(self):
		return super().get_tree_height()
	
	def filter_tree(self, k):
		return super().filter_tree(k)
	
	def min_level_sum(self):
		return super().min_level_sum()
	
	def delete_tree(self):
		return super().delete_tree()

	####################### overidden methods ############################
	def insert_node(self, n):

		# check the corresponding left/right subtree (depending on the
		# value of the node that needs to be appeneded) to determine 
		# where to add the new node in the tree
		#
		# This can be done recursively at a cost of more memory. Given
		# that the logic for the iterative approach is not too complex
		# makes this approach more favorable

		# validation check 
		if self.root == None: 
			self.root = Node.Node(n)
			return 

		# local variable 
		runner = self.root
		
		# traverse through the tree, and insert the new node in the 
		# first empty spot based on its value in relation to the 
		# already existing nodes in the tree
		while True: 
			# check if the left side needs to be further inspected
			if runner.val > n:
				# check if current node has a left child
				if runner.left: 
					runner = runner.left
				else: #add the new node there
					runner.left = Node.Node(n)
					break
			else: # inspect the right side 
				# check if node has right child 
				if runner.right: 
					runner = runner.right 
				else: 
					runner.right = Node.Node(n)
					break
				

		# since inverting the tree doesn't make sense for a binary 
	
	def get_min_max(self):

		# use the strict ordering to optimize this function. The smallest element
		# will be the left most node. Similar for the largest, being the right most
		# element in the tree

		# validation check, return (-1, -1) indicating no valid result 
		if self == None: 
			return (-1, -1)
		
		# local variables 
		min = self.root 
		max = self.root 

		# find the smallest element
		while min.left != None: 
			min = min.left
		
		# find the largest element 
		while max.right != None: 
			max = max.right

		# return the min/max values 
		return (min.val, max.val)

	def invert_tree(self):
		# search tree, this function has been overidden to simply
		# return and don't do anything

		pass 
	
	##################### newly defined methods ###########################
	def balance_bst(self): 
		# function to change a binary search tree that is more on the sparse side, 
		# to one that's as full as it can get, depending ont the number of nodes

		# validation check 
		if self.root == None: 
			print("Tree doesn't contain any nodes")
			return

		# local variables 
		# "self" is needed as the function from within the class is referred to
		bst_in_order = self.get_in_order_traversal()
		new_tree = BST()

		# helper function that will recursively split the "bst_in_order" list by 2
		# and append the middle value of each of the half list to the newly created tree
		def build_balanced_tree(root, start_idx, end_idx): 


			# base case to have the recursion bottom out. 
			# 1. Ensure the start_idx is always less than the end_idx
			# 2. If indices are the same, then this is the last 
			#    element that needs to be inserted in to the tree

			if start_idx > end_idx:
				return 

			if start_idx == end_idx: 
				new_tree.insert_node(bst_in_order[start_idx]) 
			else:
				# compute the midpoint of the current list and use that value to build the tree
				mid_point = (start_idx + end_idx)//2

				# append the current mid value
				# "self" is needed as the function from within the class is referred to
				new_tree.insert_node(bst_in_order[mid_point])

				# recursively work on the left half of the list 
				build_balanced_tree(new_tree, start_idx, mid_point - 1)

				# do the same for the right side of the list 
				build_balanced_tree(new_tree, mid_point + 1, end_idx)


		# call the helper function to get the fun started 
		build_balanced_tree(new_tree, 0, len(bst_in_order) - 1)

		# assign the passed tree to the new one
		self.root = new_tree.root

	def floor_ceil(self, k):
		# find the floor and ceiling value within the tree given a value K
		# validate the tree
		if self.root == None: 
			return None

		# local variables
		current = self.root
		floor = ceil = None

		# iterate through the tree in a binary search tree fashion 
		# and inspect the values as we go along while updaing the 
		# floor and ceiling values respectively 
		while(current):
			# check the left side if K is less than 
			# the current node
			if current.val > k: 
				ceil = current.val 
				current = current.left

			# check the right side of the tree if K is greater
			# than the current node
			elif current.val < k: 
				floor = current.val 
				current = current.right

			# current value is a match, and consequently so is 
			# the floor as well as the ceiling 
			else: 
				floor = ceil = k
				break
			
		# return the floor and ceil values 
		return (floor, ceil)

	def sorted_arr_to_bst(self, args):
		# converts a sorted array to a BST 

		# helper function 
		def build_bst(start, end, nums):

			# compute the middle 
			m = (start + end) // 2

			# base cases
			if start > end:
				return None
			elif start == end:
				return Node.Node(nums[m])
			# recursive case: keep on appending the middle element to the BST
			else: 
				current = Node.Node(nums[m])
				current.left = build_bst(start, m - 1, nums)
				current.right = build_bst(m + 1, end, nums)

			# return the current node 
			return current 

		# Local variables
		start = 0 
		end = len(args[0]) - 1 if isinstance(args[0], list) else len(args) - 1

		# "new_tree" will be receiving a "Node" object which contains the newly constructed tree
		new_tree = build_bst(start, end, args)

		# assign the newly created tree to the root of the current instance 
		self.root = new_tree

	def merge_trees(self, other):
		# merge two trees into one, while ensuring the BST order still holds

		# validation check 
		# ensure the "other" contains an object, 
		# otherwise return the first node 
		if not other: 
			return self
		
		# check whether the tree on which this method was called on is empty.
		# if so, return the other tree
		if self == None: 
			return other
		
		
		# local variables 
		merged_tree = BST()

		# get the in order traverals of both trees. This ordering will print the
		# give us a sorted list for that particular tree. Idea is to always pick 
		# the smaller value, and have that inserted in the consolidated tree.
		# Since there already is a "sorted_arr_to_bst" function we can just 
		# reuse that and eliminate code duplication 
		tree1 = self.get_in_order_traversal()
		tree2 = other.get_in_order_traversal()

		# next step is to consolidate both trees, from which the merged BST will be generated
		# since we don't know which tree has the smaller starting entry we could simply extend 
		# the two and call sort on them. 
		tree1.extend(tree2)
		tree1.sort()
		
		# call the "sorted_arr_to_bst" method on the "merged_tree" instance to have that contain the 
		# final tree
		merged_tree.sorted_arr_to_bst(tree1)

		# return the merged tree
		return merged_tree