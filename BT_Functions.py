'''
        BT_Functions.py

        Module which has functions that can be used by both BT and BST classes  

	Created: 02/25/2021

        Last Updated: 02/25/2021

	Verison: 1.0
        
        Requires: "BT.py" module

'''

######################################### Imports ###############################################
#												#
# random: Needed to generate random int values used to popluate the tree                        #
#												#
#################################################################################################
import random

######################################### Globals ###############################################
#												#
# Global values used throughout the "BT_driver" module                                          #
#												#
#################################################################################################
MAX_NUM_OF_NODES = 15
MIN_NUM_OF_NODES = 5
MIN_NODE_VAL = 1
MAX_NODE_VAL = 100


####################################### Functions ###############################################
#												#
# Functions definitions					                                        #
#       Generic functiosn that can be used for both regular binary trees, as well as bineary    #
#       search trees                                                                            #
#                                                                                               #
#       generate_values                                                                         #
#       print_tree                                                                              #
#												#
#################################################################################################
def generate_values(): 

        # local variables 
        numbers_generated = [] 
        num_nodes = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES)

        # generate the random numbers
        for i in range(num_nodes):
                numbers_generated.append(random.randint(MIN_NODE_VAL, MAX_NODE_VAL))
        
        # return the list 
        return numbers_generated

######################################## decorators #############################################
#                                                                                               #
# decorators used to reduce the code footpring by elimniating redundant code                    #
#                                                                                               #
#################################################################################################
def getter_method_decorator(func):
        # decorator for the getter functions 

        # define the wrapper function 
        def getter_wrapper(BT):

                # strip function name, and remove underscores from name
                # uppercase first letter
                # print start of message
                # print the specified order
                
                msg = func.__name__[9:].replace('_', ' ')
                msg = msg.upper()
                print(msg + " : ", end= ' ')

                # call the passed function
                func(BT)
        
        # return the wrapper function 
        return getter_wrapper

def modifier_methods_decorator(func, *args):
        # decorator for the modifer functions
        # this function has been designed to be used by many 
        # other ones, and not all of them have more than one
        # parameters. This function will check for the second
        # parameter inside the wrapper

        # define the wrapper function 
        def modifier_wrapper(BT, *args):

                # strip function name, and remove underscores from name
                # uppercase first letter
                # print start of message
                # print the specified order
                
                msg = func.__name__[5:].replace('_', ' ')

                # helper functions 
                def print_initial_status():
                        # print the tree before any modification has been done 
                        print("Tree before calling : " + "'" + msg + "'" + " function")
                        print(BT.__repr__())
                        print()
                
                def print_final_status():
                        # print the tree after the modification has been done 
                        print("Tree after calling : " + "'" + msg + "'")
                        print(BT.__repr__())
                        print()


                # currently the "balance_bst" method is an exception in how it needs to be 
                # handled inside this wrapper. 
                
                # call the passed function along with any possible arguments
                if not args: 
                        print_initial_status()
                        BT = func(BT)
                        print_final_status()
                        return BT
                else:
                        print_initial_status()
                        BT = func(BT, args[0])
                        print_final_status()
                        return BT

        # return the wrapper function 
        return modifier_wrapper       