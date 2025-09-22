"""Program that counts vowels and consonants in a string."""

def count_vowel_consonant(str):
    """Count vowels and consonants in a string.
    
    Args:
        str: Input string to analyze
        
    Returns:
        Tuple containing (vowel_count, consonant_count)
    """
    vowel_count = 0
    consonant_count = 0
    vowels = "aeiouAEIOU"
    
    for char in str:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count


print(count_vowel_consonant("hello world"))