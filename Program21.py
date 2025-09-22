"""Program that removes duplicate characters from a string."""

def remove_duplicates(st):
    """Remove duplicate characters from a string.
    
    Args:
        st: Input string with potential duplicates
        
    Returns:
        String with duplicate characters removed
    """
    seen = set()
    for char in st:
        seen.add(char)
    return ''.join(seen)


def remove_duplicates_preserve_order(st):
    """Remove duplicate characters while preserving original order.
    
    Args:
        st: Input string with potential duplicates
        
    Returns:
        String with duplicates removed, order preserved
    """
    seen = set()
    result = []
    for char in st:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


print(remove_duplicates("hello world"))
print(remove_duplicates_preserve_order("hello world"))