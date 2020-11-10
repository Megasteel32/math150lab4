from sympy import *
from numpy import power

x = symbols("x")
e = 2.71828183
expression = 2 * e**(x-4) + 3
plot1 = plot(expression)

leftBIG = -1, -10, -100, -1000, -1000000
rightBIG= 1, 10, 100, 1000, 1000000

for poop in range(len(leftBIG)):
    tempval = 0
    tempval = 2 * power(e, (leftBIG[-poop]-4)) + 3
    print(tempval)

for crap in range(len(rightBIG)):
    tempval = 0
    tempval = 2 * power(e, (rightBIG[-crap]-4)) + 3
    print(tempval)

limitofexp = limit(expression, x, oo)
print(limitofexp)
limitofexp = limit(expression, x, -oo)
print(limitofexp)

# Nate I am so sorry this code is complete shit im pulling libraries out of my ass right now trying to make this work
# This week has been a doozy and its a monday night. fml.

# poopy hasdufkhsadkjf