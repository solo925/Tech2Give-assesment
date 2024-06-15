# Question 3: Design a function that takes a string or sequence of characters as input and
# returns the character that appears most frequently.
# Eg 11189 => '1'
# hello => 'l'

def most_frequent_character(s):
    #  I create a dictionary to keep track of character frequencies
    frequency = {}
    
    # I then  iterated over each character in the input string
    for char in s:
        # Increment the count for the character in the dictionary i.e if i already have a character
        # in the frequency dictionary the number of chacters will be increnented by one else the value /
        # frequency will just be 1
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # initialized max_count to 0 and most frequent to none and iterate to compare each frequecy do determine the largest
    max_count = 0
    most_frequent = ''
    for char in frequency:
        if frequency[char] > max_count:
            max_count = frequency[char]
            most_frequent = char
    
    return most_frequent

# printing the output
print(most_frequent_character("solomon"))  
print(most_frequent_character("11189"))
print(most_frequent_character("hello"))
print(most_frequent_character("aabbbcc")) 

