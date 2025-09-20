"""Program to extract unique elements from a list of numbers."""

def get_unique_elements(nums):
    """Return unique elements from a list of numbers.
    
    Args:
        nums: List of numbers that may contain duplicates
        
    Returns:
        Set containing only the unique elements from the input list
    """
    return set(nums)


print(get_unique_elements([1, 1, 2, 3, 4]))