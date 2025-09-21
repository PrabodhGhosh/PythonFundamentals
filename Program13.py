"""Dictionary sorting utilities.

This module provides functions to sort dictionaries by keys and values.
"""

def sort_keys(data):
    """Return a list of dictionary keys sorted in alphabetical order."""
    return sorted(data.keys())

def sort_values(data):
    """Return a dictionary sorted by values in numerical order."""
    return dict(sorted(data.items(), key=lambda x: x[1]))

print(sort_keys({'c': 3, 'a': 1, 'b': 2}))
print(sort_values({'c': 3, 'a': 1, 'b': 2}))