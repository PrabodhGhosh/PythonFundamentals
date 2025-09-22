"""Program that reverses a given string."""

def reverse_string(str):
    """Reverse a given string.
    
    Args:
        str: String to reverse
        
    Returns:
        Reversed string
    """
    return str[::-1]


print(reverse_string("hello"))