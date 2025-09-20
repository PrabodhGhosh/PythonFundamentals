"""Program to find the larger of two numbers."""

def bigger_of_two(num1, num2):
    """Return the larger of two numbers.
    
    Args:
        num1: First number to compare
        num2: Second number to compare
        
    Returns:
        The larger of the two input numbers
    """
    if num1 > num2:
        return num1
    return num2


print(bigger_of_two(5, 2))