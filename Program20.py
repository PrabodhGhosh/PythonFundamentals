"""Program that checks if a string contains only digits."""

def check_only_digits(st):
    """Check if a string contains only digits.
    
    Args:
        st: Input string to check
        
    Returns:
        True if string contains only digits, False otherwise
    """
    return st.isdigit()


print(check_only_digits("1234"))