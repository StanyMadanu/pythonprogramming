#Program to accept list of words and get a line of text by using reduce()

import functools

#main program
print("Enter list of words separated by comma (,)")
lst = [val for val in input().split(",")] #list comprehension

res = functools.reduce(lambda w1,w2: w1+" "+w2, lst)
print(res)