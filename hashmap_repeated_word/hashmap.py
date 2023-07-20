def repeated_word(s):
    # Step 1: Split the input string into words
    words = s.split()

    # Step 2: Create a hashmap to store word frequencies
    word_freq = {}

    # Step 3: Traverse through each word and update the hashmap
    for word in words:
        # Convert the word to lowercase to handle case-insensitivity
        word = word.lower()
        
        # Increment the frequency count in the hashmap
        word_freq[word] = word_freq.get(word, 0) + 1
        
        # Step 4: Check if the current word is repeated
        if word_freq[word] > 1:
            return word

    # If no repeated word found, return None
    return None
input_string = "I love to code in Python. Python is awesome and Python is fun."
result = repeated_word(input_string)
print(result)  # Output: "python" (the first repeated word in the string)
