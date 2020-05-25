# Project Euler Problem 112
"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for
example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525)
are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers
is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%."""

import timeit

def isBouncy(number):
    #number = "22100"
    digitIsIncreasing = []
    for i in range(0,len(number)-1):
        current = number[i]
        next = number[i+1]

        if current < next:
            digitIsIncreasing.append(1);
        if current > next:
            digitIsIncreasing.append(-1);
        if current == next:
            digitIsIncreasing.append(0);

    isInceasing = all([j!=-1 for j in digitIsIncreasing])
    isDecreasing = all([j!=1 for j in digitIsIncreasing])
    isBouncy = not isInceasing and not isDecreasing
    return isBouncy

bouncies = []
percentage = 0.0
percentageTarget = 0.99
for n in range(1,200):
    #start = time.time.perf_counter()
    if isBouncy(str(n)):
        bouncies.append(n)
        percentage += (1-percentage)/n
    else:
        percentage += (0-percentage)/n
    if percentage > percentageTarget :
        break
    #end = time.time.perf_counter()
    #print(end-start)

print("Bouncy number", bouncies[-1], "reaches", "{:.2f}%".format(percentage*100))

# Die Zahl ist um 1 zu hoch!!!


