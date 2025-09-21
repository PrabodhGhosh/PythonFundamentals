"""Return a new set containing elements common to both input sets."""

def  common_elements(set1, set2):
    final_set = set()
    for element in set1:
        if element in set2:
            final_set.add(element)
    return final_set


print(common_elements({1,2,3},{2,3,4}))

