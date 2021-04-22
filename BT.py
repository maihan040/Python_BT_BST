'''
	BT.py

	Module to define the "Binary Tree" class. This module will contain the root "node" element, 

	as well as the various methods simulating all the basic operations that can be peformend on a 

	binary tree

	Created: 02/23/2021

	Last Updated: 02/24/2021

	Verison: 1.0
'''

#################################### Class Definition ###########################################
#                                                                                       	#
# Note: Tree will initially contain an empty Node object, unless the user specifies a value	#
#                                                                                       	#
#       Should the user not supply a data value for the root of the tree, then the value will  	#
#	default (to None) in the init method							#
#                                                                                       	#
#################################################################################################

#################################### Methods defined ############################################
#                                               						#
# Following methods are defined inside the class definition:                            	#
#												#
#	//MODIFYING METHODS//									#
#   	insert__node                                        					#
#	invert__bin_tree									#
#	delete_tree 										#
#	filter_tree 			 							#
#												#
#	//GETTER METHODS//									#
#	get_pre_order_traversal									#
# 	get_in_order_traversal									#
# 	get_post_order_traversal								#
#	get_level_order_traversal								#
#	get_tree_height										#
#	get_min_max										#
#	get_min_level_sum 		 							#
#												#
#################################################################################################

######################################### Imports ###############################################
#												#
# Node.py: Node used to build the the individual nodes of the binary tree                     	#
# queue:   Used for the append method 								#
# sys:     Used to obtain max and min INT values						#
#												#
#################################################################################################
import Node
import queue
import sys

class BT:
                                           						 										
	def __init__(self, val = None):

		# This will initialize a new root element of the tree when a new instance
		# is created for the first time
		
		# Checks to see whether the user supplied a value for the value and will take the 
		# appropriate action in constructing the node     	
		if val == None: 
			self.root = None
		else: 
			self.root = Node.Node(val)


	def __repr__(self):

		# delegate the function to the tree's root (Node) instance
		# if the tree contains any nodes
		if isinstance(self.root, Node.Node):
			return self.root.__repr__()
		else: 
			return f"(Tree is empty)"
	
	#
	# Insert node
	#
	def insert_node(self, val): 

		# method to add a node to the tree. Since a regular binary tree doesn't follow a specfiied 
		# order, new nodes will be added either to the first node whose left child is empty, or the
		# first node whose right child is empty. Which ever comes first

		# 				Validation check 
		# check whether the passed tree is empty. In which case all that's needed is to have the 
		# root contain "val" and the method is done with it's job
		if self.root == None: 
			self.root = Node.Node(val)
			return
		
		# local variables 
		q = queue.Queue()
		q.put(self.root)

		# iterate through the tree until the first available slot has been found
		# whenever a left branch has been chosen, append the right child to the "q".
		# This is so that we can search the right side, should the left be ruled out
		while q: 

			# pop the element from the queue
			current_node = q.get()

			# check if left child is empty. This would be the first node whose 
			# left child is empty, hence we found the spot. Otherwise store the 
			# left child
			if current_node.left == None: 
				current_node.left = Node.Node(val)
				break 
			else: 
				q.put(current_node.left)
			
			# check the same for the right child 
			if current_node.right == None: 
				current_node.right = Node.Node(val)
				break 
			else: 
				q.put(current_node.right)

	#
	# Invert tree
	#
	def invert_tree(self):

		# Function to invert the tree. After this function the BST will be a mirror reflection of what	#
		# it was before this function was called.

		# validation check 
		if self == None: 
			print("Tree doesn't contain any nodes")
			return

		# helper function which will swap the child nodes of each respective node 
		def invert(node):

			# base case
			if node == None: 
				return

			# proceed in a post order fashion while inverting the children of each node
			invert(node.left)
			invert(node.right)

			# main operation, swap left and right children
			temp = node.left
			node.left = node.right
			node.right = temp

		# call the helper function 
		invert(self.root)
	
	#
	# Delete tree
	#
	def delete_tree(self):
		# set the root of the tree to "None" and have the garbage collector 
		# take care of the rest 
		self.root = None
	
	
	#
	# filter tree
	#
	def filter_tree(self, k):
		# given a value "k" filter the leafs of the tree that have "k" in their data field
		# as well as parents who also have value "k" and whose childrens have been removed
		# that is only remove the parent if they become a leaf after their child/s have been
		# removed

		# validation check 
		if self.root == None: 
			return root

		# helper method, check if the current node is in violation, meaning it should be removed
		def is_leaf_k(node):
			if node.left == None and node.right == None and node.val == k:
				return True
			else: 
				return False

		# helper function to process the individual tree nodes
		# returns a boolean where "True" indicates that the child 
		# in question should be removed, and "False" indicates
		# that the child does not need to be removed
		# 
		# this method will proceed in a post order fashion through the tree
		# as parent may potentially need to be deleted as well
		def process_leafs(node): 

			# base cases
			if node == None: 

				# return false indicating that this node 
				# doesn't need to be removed
				return False

			# check if leaf is in violation 
			if is_leaf_k(node):

				# return true as this node does
				# need to be removed
				return True
			else:
				# recursive case, compute the node's left and right side 
				left = process_leafs(node.left)
				right = process_leafs(node.right)

				# check whether a child needs to be removed 
				if left: 
					node.left = None
				if right: 
					node.right = None

				# check whether the current parent needs to be removed if it
				# finds itself now being in violation 
				if is_leaf_k(node):
					return True

		# call the helper function 
		process_leafs(self.root)

	#		
	# Traversal Functions 
	#
	def get_pre_order_traversal(self):
		# return nodes in the following order
		# parent node value, left child node value, and right child node value 
		#
		# Output: list object containing the pre order arrangment of the nodes within the tree

		#local variables
		order = []

		# helper function that will recursively traverse through the tree per the specified order
		def walk_bst_preorder(node):

			# base case
			if node == None: 
				return 

			# append the current node to the list  
			order.append(node.val)

			# move on to left child 
			walk_bst_preorder(node.left)

			# move on to right child 
			walk_bst_preorder(node.right)

		# call the recursive helper method 
		walk_bst_preorder(self.root)

		# return the list 
		return order
	
	def get_in_order_traversal(self):
		# return nodes in the following order
		# left child node value, parent node value, and right child node value  
		#
		# Output: list object containing the in order arrangment of the nodes within the tree

		# local variables 
		order = [] 

		# helper function that will recursively traverse through the tree per the specified order
		def walk_bst_inorder(node):     
		
			# base case 
			if node == None: 
				return 

			# move on to left child 
			walk_bst_inorder(node.left)     

			# append the current node to the list 
			order.append(node.val) 

			# move on to the right child  
			walk_bst_inorder(node.right)

		# call the helper function 
		walk_bst_inorder(self.root)  

		# return the list 
		return order

	def get_post_order_traversal(self):
		# return nodes in the following order
		# left child node value, right child node value, and parent node value
		#
		# Output: list object containing the post order arrangment of the nodes within the tree
	
		#local variables
		order = [] 
	
		# helper function that will recursively traverse through the tree per the specified order
		def walk_bst_postorder(node):
			
			# base case
			if node == None: 
				return 
			
			# move on to the left child 
			walk_bst_postorder(node.left)
			
			# move on to the right child 
			walk_bst_postorder(node.right)
			
			# append the current node to the list 
			order.append(node.val)
		
		# call the helper function 
		walk_bst_postorder(self.root)
		
		# return the list 
		return order
	
	def get_level_order_traversal(self):
		# return nodes level by level 
		#
		# Output: list object containing the level order arrangment of the nodes within the tree
	
		# local variables
		order = []
		q = queue.Queue()
		q.put(self.root)

		# keep on adding each child nodes for the given node until the queue is empty
		while q.qsize() > 0:

			# get the current element from the queue 
			current_node = q.get()

			# append that node to the "order" list 
			order.append(current_node.val)

			# add left child to the queue if present
			if current_node.left:
				q.put(current_node.left)
			
			# add right child to the queue if present 
			if current_node.right:
				q.put(current_node.right)
		
		# return the list 
		return order 

	#
	# get_tree_height
	#
	def get_tree_height(self):
		# compute the height of the tree

		# validation check 
		if self == None: 
			return 0

		# local variables 
		height = 0

		# helper function which will recursively call itself to compute the height of the tree
		# essentially this will compare the heights of the children for each node picking the
		# max height between the right/left sub tree
		def compute_height(node): 

			# base case when the recursion bottoms out: 
			if node == None: 
				return 0

			# local variables 
			left_height = compute_height(node.left)
			right_height = compute_height(node.right)

			# return the max of the two plus 1 to account the level of the current node 
			return max(left_height, right_height) + 1

		# call the helper function to start the computation 
		height = compute_height(self.root)

		# return the computed height 
		return height

	#
	# get_min_max
	#
	def get_min_max(self):
		# method to find the smallest/largest elements that are in the tree
		#
		# Output: returns tuple containing both values 

		# local variables
		q = queue.Queue()
		min = sys.maxsize
		max = -sys.maxsize - 1

		# put the root of the tree inside the queue
		q.put(self.root)

		# validation check 
		if q.qsize() == 0: 
			return (0, 0)
		
		
		# traverse through the tree in a pre order fashion and inspect each node 
		# whether they are min values 
		while q.qsize() > 0:

			# remove an element from the queue
			runner = q.get()

			# inspect current node 
			if runner.val >= max:
				max = runner.val 
			if runner.val < min: 
				min = runner.val 
			
			# add children to the queue to process those next 
			if runner.left: 
				q.put(runner.left)
			
			if runner.right: 
				q.put(runner.right)
		
		
		# return the findings 
		return(max, min)

	#
	# min level sum
	#
	def get_min_level_sum(self): 
		# find the level of the tree that has the smallest sum 
		# and return that sum 

		# base case check 
		if self.root == None: 
			return -1 

		# local variables 
		# store the root of the tree as a starting point 
		q = [self.root] 
		min_sum = self.root.val # assume the root val is the lowest sum prior to starting the iteration
		

		# iterate through each node in "q" and keep track of the 
		# children in order to build the next level down 
		while q: 

			child_level = [] 
			level_sum = 0

			# iterate through each node for a given level 
			for node in q: 

				# check if node has left child 
				if node.left:
					child_level.append(node.left)
					level_sum += node.left.val

				# check whether node has right child 
				if node.right: 
					child_level.append(node.right)
					level_sum += node.right.val

			# determine whether the last processed level is the minimum 
			# check whether level_sum is "0" as the leafs wil return 0 
			# for their subsequent level 
			if level_sum != 0:
				min_sum = min(min_sum, level_sum)

			# have q point to the new level for the next run 
			q = child_level 

		# return the minium 
		return min_sum