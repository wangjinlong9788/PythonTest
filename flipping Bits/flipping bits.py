#!/bin/python3

import math
import os
import random
import re
import sys
import math
#import numpy as np
# Complete the flippingBits function below.
def flippingBits(n):
    bi=[]
    b=n
    bi32=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while(b!=0):
      bi.append(b%2)
      b=math.floor(b/2)
    for j in range(len(bi)):
      bi32[31-j]=bi[j]
    

    for i in range(len(bi32)):
      if bi32[i]:
        bi32[i]=0
      else:
        bi32[i]=1
    oct=0
    for i in range(len(bi32)):
       oct=oct+bi32[i]*2**(31-i)
    return oct
         

    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
