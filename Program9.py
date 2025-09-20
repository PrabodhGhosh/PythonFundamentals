"""Program that counts the frequency of each word in a user-provided list."""

def word_frequency():
    """Count the frequency of each word in a user-provided list.
    
    Returns:
        Dictionary with words as keys and their frequencies as values
    """
    words_input = input("Enter words separated by spaces: ")
    words = words_input.split()
    
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency


print(word_frequency())
