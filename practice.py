# # def repeat_hello(n):
# # 	if n > 0:
# # 		print("Hello")
# # 		repeat_hello(n - 1)
		
# # repeat_hello(5)

# # def repeat_hello_iterative(n):
# # 	while n > 0:
# # 		n -= 1
# # 		print("Hello")
		
	

# # repeat_hello_iterative(5)

# '''
# understand
# return the factorial of the parameter inside the function 
# base case is 0, where the factorial is 1
# '''
# # def factorial(n):
# # 	if n == 0:
# # 		return (1)
	
# # 	return n * factorial(n-1)
# # print(factorial(5))

# '''
# understand 
# traverse through a list and add the values and then return the sum
# '''

# # def sum_list(lst):
# #     if len(lst) == 0:
# #         return (0)
# #     else:
# #         return lst[0] + sum_list(lst[1:]) # add each value to the previous value
# # print(sum_list([1,2,6,7]))
# # time complexity 

# '''
# recursive power of 2
# test case
# is_power_of_two(4)
# output: True 

# '''


# def is_power_of_two(n):
#     if n ==1:
#         return True
#     elif n%2 != 0 or n ==0:
#         return False
#     else:
#         return is_power_of_two(n/2)
    
# print(is_power_of_two(78))


# def binary_search(lst, target):
# 	left_pointer = 0
# 	right_pointer = len(lst)-1

	
# 	middle = len(lst)/2 
# 	while left_pointer < right_pointer:
# 		# Find the middle index of the array
		
# 		if len(lst)/2 == target:
# 			return (middle)
# 		# Else if the value at the middle index is less than our target value:
# 			# Update pointer(s) to only search right half of the list in next loop iteration
# 		# Else
# 			# Update pointer(s) to only search left half of the list in next loop iteration
	
# 	# If we search whole list and haven't found target value, return -1


# '''
# find the target substring within the main string

# '''
# def count_substring(s, sub):
#     if sub not in s or len(s) == 0:
#         return 0
#     if sub in s and len(s) <= len(sub):
#         return 1
#     else:
#         x = s.find(sub)
#         return 1 + count_substring(s[x+1:], sub)
# print(count_substring("abcdeabcde", "abc"))

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node_one = TreeNode(1)
node_two = TreeNode(2)
node_three = TreeNode(5)
node_four = TreeNode(4)
node_five = TreeNode(3)

node_one.left = node_two    # Node two is the left child of node one
node_one.right = node_three
node_two.left = node_four 
node_two.right = node_five 

def left_most(root):
   
    current = root
    if root == None:
        return None
    while current != None and current.left != None:
        current = current.left
        
    return current.val
def size(root):
   current = root 
   size = 0
   while current != None and current.left != None or current.right != None:
   current.left



# def sumCheck( node_two, node_three, node_one):
#         if node_two.val + node_three.val == node_one.val:
#             return True
#         else:
#             return False


# print( "root:" , node_one.val , "left:", node_two.val, "right:", node_three.val)
print (node_two.left)
print (left_most(node_one))



for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

        # rember the fizzBuzz! This should probably be done in the future but
        # for now, I'll add it here for demonstration purposes.
        if i % 15 == 0:
            print("FizzBuzz") 
            # Note: This will print "FizzBuzz" twice if the number is divisible by both 3 and 5,
            # so we could adjust the code to only print once.
            # For example, we could replace the print("FizzBuzz") line with:
            # print("FizzBuzz once")
            # or even:
            # print("FizzBuzz", end=" ")
            # if i < n:
            #     print(", ", end="")
            # else:
            #     print(".")
             
             