'''
Created on Jul 18, 2019
NaKyung Lee


Returns n-th fibonacci number
Prompt with n
The sequence starts with 1, 1, 2, ...

'''

n = input(enter n value)

fib = [1, 1]

while n > len(fib):
    fib.append(fib[-1]+fib[-2])

print(fib[-1])