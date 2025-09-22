"""Program that removes all whitespace from a given string."""

def remove_whitespace(str):
    """Remove all whitespace from a string.
    
    Args:
        str: Input string with whitespace
        
    Returns:
        String with all whitespace removed
    """
    return str.replace(" ", "")

print(remove_whitespace("hello world"))