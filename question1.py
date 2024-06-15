# Question 1: Design a function that reverses the digits of an integer. 
# For example, 50 should become 5 and -12 should become -21.

def reverse_integer(number):
    #  I converted the integer to a string and checked if it's negative
    sign = -1 if number < 0 else 1
    number_str = str(abs(number))
    
    # I reverse the string and converted it back to an integer with the correct sign
    reversed_number = int(number_str[::-1]) * sign
    return reversed_number

# I then tested the string to accertain my solution
print(reverse_integer(50))   
print(reverse_integer(-12))  
