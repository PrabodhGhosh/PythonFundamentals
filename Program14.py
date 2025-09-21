"""Program to find the second-largest number in a list.

This program takes a list of numbers and returns the second-largest number.
"""

def get_second_largest(elements):
    """Return the second-largest number in the list."""
    largest = second_largest = elements[0]
    
    for element in elements:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest and element != largest:
            second_largest = element
    
    return second_largest

print(get_second_largest([1, 5, 3, 9, 2]))  # Should return 5
print(get_second_largest([10, 10, 5]))      # Should return 5