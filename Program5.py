"""Program to calculate the factorial of a given number."""

# Write a function that calculates the factorial of a given number.

def find_factorial(num):
    """Calculate the factorial of a given number.
    
    Args:
        num (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of the given number (num!)
    """
    # Initialize result to 1
    val = 1
    
    # Multiply by each number from 1 to num
    for i in range(1, num + 1):
        val *= i
    
    return val


# Test the function
print(find_factorial(5))  # Expected output: 120