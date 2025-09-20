"""Program to sort a list of tuples by score in descending order."""

def sort_list_of_tuples(tuples):
    """Sort a list of (name, score) tuples by score in descending order.
    
    Args:
        tuples: List of tuples where each tuple contains (name, score)
        
    Returns:
        List of tuples sorted by score in descending order
    """
    return sorted(tuples, key=lambda x: x[1], reverse=True)


# Test the function
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 96)]
print(sort_list_of_tuples(students))