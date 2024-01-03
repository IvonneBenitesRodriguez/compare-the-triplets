#Using python: 
# Function zip
#it is used to combine elements from 2 or more iterables into tuples.

# Tuples:
# A tuple is a collection data type that is similar to a list.
# Tuples are immutable => their elements cannot be changed or modified
# after the tuple is created.
# Tuples are defined using parentheses ()

# Zip function creates an iterator that produces tuples.
# Each tuple contains elements from corresponding positions in the input
# iterables.
# Example of using zip function in python
a = [1,2,3]
b = ['a', 'b', 'c']

# Using zip to combine elements from a and b
combined = list(zip(a, b))
print(combined)
# output : [(1, 'a'), (2, 'b'), (3, 'c')]

# but we are using also list function:
# It is a built-in function that can be used to create a list
# from an iterable.
# Example:
# Creating a list from a string
string_example = 'hello'
list_from_string = list(string_example)
print(list_from_string)

['h', 'e', 'l', 'l','o']

#Solution of the hackerrank challenge 
def compareTriplets(a,b):
    alice_score, bob_score = zip(*[(1,0) if x > y 
                                   else (0,1) if x < y 
                                   else (0,0) for x, y in zip(a,b)])
    return [sum(alice_score), sum(bob_score)]

#Example usage:
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a,b)
print(''.join(map(str, result)))

# map(str, result) is used to convert each element in
# the result list to a string.
# this is necessary because the join method expects 
# an iterable of strings as its arguments.

# map function in Python is a built-in function that applies a specified 
# function to all items in an iterable (list, tuple, or string) and return 
# an iterator that produces the results.


