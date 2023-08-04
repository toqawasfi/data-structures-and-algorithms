from hashmap_repeated_word.hashmap import repeated_word

# Test cases for repeated_word function
def test_repeated_word():
     # Test case 1
    str = "Once upon a time, there was a brave princess who..."
    assert repeated_word(str) == "a"

    # Test case 2
    input_string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."
    assert repeated_word(input_string2) == "it"

   
