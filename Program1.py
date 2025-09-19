"""Program to determine if a number is odd or even."""

def find_odd_even(num):
    """Return whether a number is odd or even.
    
    Args:
        num (int): The number to check
        
    Returns:
        str: Message indicating if number is odd or even
    """
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


# Test cases
print(find_odd_even(5))
print(find_odd_even(10))
print(find_odd_even(0))