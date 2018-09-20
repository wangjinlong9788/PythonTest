#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
"""def minimumPasses(m, w, p, n):
    ps=1
    n0=m*w
    if n0>=n:
        return ps
    while n0+(m)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
"""

#Greedy Algorithm Approach

### IMPORTS ###
from math import ceil

### FUNCTIONS ###
def Purchaser(Machine,Worker,count):

#idea behind count > remainder loop below:
#we want to spend all of our money in each round (greedy) because #in the next round it will have a higher multiplier effect on count.
#optimally, to get the most "bang for our buck" we would want Machine == Workers because this gives the highest count.
#Given that the two numbers are equal, we would want to increment #them evenly. If the amount of SpendingMoney is not even, then 
#Without loss of generality we can give it to one of the factors (either Machine's or Worker's).

    SpendingMoney = count//Price
    remainder = count%Price    
    while count > remainder:
        if Machine < Worker:
            diff = Worker - Machine
            if diff >= SpendingMoney:
                Machine += SpendingMoney
                count = remainder
                break
            else:
                Machine += diff
                SpendingMoney -= diff
                count -= Price*diff
        elif Worker < Machine:
            diff = Machine - Worker
            if diff >= SpendingMoney:
                Worker += SpendingMoney
                count = remainder
                break
            else:
                Worker += diff
                SpendingMoney -= diff
                count -= Price*diff
        else:
            if SpendingMoney % 2 == 0:
                Worker += SpendingMoney//2
                Machine += SpendingMoney//2
                count = remainder
                break
            else:
                Worker += SpendingMoney//2
                Machine += SpendingMoney//2 + 1
                count = remainder
                break
    return Machine,Worker,count

def MinResource(counter, count, Candy, Machine, Worker, minimum):
    #Checks the number of resources needed to generate our solution at this point
    #We use ceiling because there are no partial iterations
    RawIteration = counter + ceil((Candy - count) / (Machine * Worker)) 
    if minimum > RawIteration:
        minimum = RawIteration
    return minimum

def IteratorMatcher(Machine,Worker,counter,count):
    CounterAdder = ceil((Price - count)/(Machine * Worker))
    countAdder = CounterAdder * (Machine*Worker)
    return counter + CounterAdder, count + countAdder

# ======Inputs======
#Machine: the number of machines
#Worker: the number of workers
#Price: the price of buying one machine or hiring one worker
#Candy: the number of candies Karl must make

### INPUTS ###
Machine, Worker, Price, Candy = map(int,input().split())
count, counter = 0, 1
minimum = 1e12

### TRANSFORMATION ###
while count < Candy:
    count += Machine * Worker
    minimum = MinResource(counter, count, Candy, Machine, Worker, minimum)
    #The code will not conventionally exit the loop because we spend all of our resources after each round
    #Therefore we need to add this break short-circuit
    if count >= Candy:
        break
    counter, count = IteratorMatcher(Machine,Worker,counter,count)
    Machine,Worker,count = Purchaser(Machine,Worker,count)
    #After we have spent all of the candies we have created, its time to increment our counter for the next round
    counter += 1
    
### OUTPUT ###
print(min(counter,int(minimum)))
