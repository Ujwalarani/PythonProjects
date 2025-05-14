"""Challenge: Optimize the function to handle large input lists efficiently.
==============================
Description: Develop a function called find_common_elements that takes two lists as input
and returns a new list containing elements that are common to both input lists."""

def find_common_elements(a, b):
    a = set(a)
    b = set(b)
    # using Set Intersection method to get common elements and converting back to list
    common_list = list(a & b)
    return common_list
while True:
    # use split() method to separate the words/numbers at the spaces as individual elements
    list1 = input("Enter elements for the first list, separated by commas: ").split(",")
    list2 = input("Enter elements for the second list, separated by commas: ").split(",")
    print(find_common_elements(list1, list2))