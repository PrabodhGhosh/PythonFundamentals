"""Program to check if a list is sorted in ascending order.

This program provides an efficient function to determine if a list
is already sorted without creating a new sorted copy.
"""

def check_if_sorted(elements):
    """Return True if the list is sorted in ascending order, False otherwise."""
    if not elements:  # Handle empty list
        return True
    
    for i in range(len(elements) - 1):
        if elements[i] > elements[i + 1]:
            return False
    return True


# Test cases
print(check_if_sorted([1, 2, 3, 4, 5]))     # True
print(check_if_sorted([1, 2, 3, 4, 5, 1]))  # False
print(check_if_sorted([]))                   # True (empty list)
print(check_if_sorted([5]))                  # True (single element)
print(check_if_sorted([1, 1, 2, 3]))        # True (duplicates allowed)
