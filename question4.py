# Question 4: Design a function that determines whether a given string is a pangram.
# A pangram is a sentence or phrase containing every letter of the alphabet at least once.
# Punctuation and case are typically ignored. For example, the string 
# "The quick brown fox jumps over the lazy dog" is a pangram, while "Hello, world!" is not.

def is_pangram(s):
    # Convert the string to lowercase and create a set of unique characters
    s = s.lower()
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in s:
        # If the character is a letter, add it to the set
        if 'a' <= char <= 'z':
            unique_chars.add(char)
    
    # Check if the set contains all 26 letters of the alphabet
    return len(unique_chars) == 26


print(is_pangram("The quick brown fox jumps over the lazy dog")) 
print(is_pangram("Hello, world!"))  
print(is_pangram("Pack my box with five dozen liquor jugs")) 
