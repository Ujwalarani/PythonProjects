"""Challenge: Use a loop structure to compare characters from
both ends of the string to determine whether it is a palindrome.
===================================
Description: Write a program that prompts the user to enter a string and then
checks whether it is a palindrome. A palindrome is a word, phrase, number, or
other sequence of characters that reads the same forward and backward."""
"""
Madam
Malayalam
1234321
9876.789
Yo, banana boy!
Step on no pets.
Never odd or even.
Was it a car or a cat I saw?
No lemon, no melon.
"""
while True:
    value = input("Enter a word, phrase, number, or other sequence of characters: ")
    print("Value entered:", value)
    value = value.lower()
    print("value after converting to lower case:", value)
    value = (value.replace(" ", "").replace(",", "")
             .replace("!", "").replace("?", "").replace(".",""))
    print("value after removing spaces:", value)
# Slice the word syntax: Str_Name[start: end: step]
    rev_value = value[::-1] # step given as -1 so the slice starts from the end of a word
    print("Reversed value is", rev_value)

    if rev_value == value:
        print("Given value is a Palindrome")
    else:
        print("Given value is NOT a Palindrome")