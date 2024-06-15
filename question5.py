# Question 5: Design a function that takes a list of integers as input.
# The function should return True if the list contains two consecutive threes (3 next to a 3) anywhere
# within the list. Otherwise, it should return False.
# For example, the function should return True for [1, 3, 3] and False for [1, 3, 1, 3].

def consecutive(integers):
    # Iterate through the list, checking each pair of consecutive elements
    for i in range(len(integers) - 1):
        # Check if both the current element and the next element are 3
        if integers[i] == 3 and integers[i + 1] == 3:
            return True
    # If no consecutive threes were found, return False
    return False

#calling the function and printing th otptu to the console
print(consecutive([1, 3, 3])) 
print(consecutive([1, 3, 1, 3])) 
print(consecutive([3, 3, 1, 3, 3]))  
print(consecutive([1, 2, 3, 4, 5])) 
