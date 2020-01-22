'''
Created on Jul 18, 2019
NaKyung Lee


Prompt with 2 numbers: a and b
Returns a list of multiples of a below b

'''

n = 1
m = []
a = int(input("enter a value"))
b = int(input("enter b value"))

while n<b:
     if n%a==0:
       m.append(n)
     n += 1

s = ''
for element in m:
    s += str(element)+" "
    
print(s)