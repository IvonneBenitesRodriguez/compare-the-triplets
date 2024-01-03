def compareTriplets(a,b):
    return [sum(x > y for x, y in zip(a,b)), 
            sum(x < y for x, y in zip(a,b))]

#Example usage
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a,b)
print(*result)

# Methods used
# for loop : used to perform actions repeatedly for each item in the iterable
# in this case I am using for in 

# sum function is a built-in function that takes an iterable 
# such as (a list, tuple, etc) an returns the sum of all the elements
# iterable.

# zip function is used to combine elements from two or more iterables into
# tuples.
# it is used to pair up elements from arrays a and b

#list function is used to create a new list.

#map function is used to apply a specified function to all items 
# in an iterable and return an iterator that produces the result.

#split function is used to split a string into a list of substrings based
# on a specified delimiter.

#print function is used to output data to the console or to a file. 
 # Example:
# print(*result) 
# I am printing all the elements of the result list with a space between them


