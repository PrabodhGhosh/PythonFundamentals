"""Program to calculate the sum of all numbers in a list."""

# Create a function that takes a list of numbers and returns the sum of all elements.

def add_all_numbers(list_of_numbers):
    """Calculate the sum of all numbers in a list.
    
    Args:
        list_of_numbers (list): List of numbers to sum
        
    Returns:
        int/float: Sum of all elements in the list
    """
    # Initialize sum variable
    val = 0
    
    # Iterate through each number and add to sum
    for i in list_of_numbers:
        val += i
    
    return val


# Test the function
print(add_all_numbers([1, 2, 3.4]))