def repeated_word(string):
    word_list = string.split()  # Split the string into a list of words
    word_count = {}  # Dictionary to store word counts
    
    for word in word_list:
        if word in word_count:
            return word  # Return the first repeated word
        else:
            word_count[word] = 1
    
    return None  # Return None if no repeated word is found
sentence = "The quick brown fox jumps over the lazy dog"
result = repeated_word(sentence)
print(result)  # Output: None

sentence = "The quick brown fox jumps over the quick dog"
result = repeated_word(sentence)
print(result)  # Output: quick
