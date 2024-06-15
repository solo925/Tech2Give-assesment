# Question 6: Design a function that takes a sentence as input and returns a new
# sentence with the words reversed in the same order that Master Yoda would use.

def reversed(sentence):
    # remove extra spaces to form word
    words = sentence.split()
    
    # Reversing
    reversed_words = words[::-1]
    
    # Join the reversed words into a new sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# printing the output
print(reversed("I am home")) 
print(reversed("May the Force be with you"))  
