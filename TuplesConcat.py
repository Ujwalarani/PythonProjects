"""Challenge: Ensure that the function works correctly with tuples of different lengths with error handling.
=============================================
Description: Create a function called concat_tuples that takes two tuples as input
and returns a new tuple containing all elements from both input tuples."""


# function to concatenate tuples
def concat_tuples(tup1, tup2):
    return tup1 + tup2
while True:
    try:
        #eval() method allows to directly input a tuple in standard tuple syntax
        tuple1 = eval(input("Enter a tuple1: "))
        tuple2 = eval(input("Enter a tuple2: "))
        #The isinstance() function returns True if the specified object is of the specified type, otherwise False
        if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
            raise TypeError("Error: Inputs must be tuples, not lists!")
        # Calling the function in print()
        print(concat_tuples(tuple1, tuple2))
    except SyntaxError as e:
        print(e)
    except NameError as n:
        print(n)
    except TypeError as t:
        print(t)