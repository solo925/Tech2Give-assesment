# Question 2: Write a recursive function to calculate the factorial of a number

def factorial(number):
    # determining the Base case i.e the factorial of 0 or 1 is 1
    if number == 0 or number == 1:
        return 1
    # defining the recursive case i.e number * factorial of (number-1)
    else:
        return number * factorial(number - 1)

# then i called the function while printing the expected factorial outputs
print(factorial(5))  
print(factorial(0)) 
print(factorial(3))  
print(factorial(1))  
