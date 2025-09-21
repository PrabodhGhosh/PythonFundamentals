"""Program to filter strings by length.

This program takes a list of strings and returns a new list containing
only the strings that have a length greater than 5.
"""

def get_strings(list_of_strings):
    """Return a list of strings with length greater than 5."""
    strings = []
    for element in list_of_strings:
        if len(element)>5:
            strings.append(element)
    return strings
            

print(get_strings(["apple","boy","girls","meadows"]))