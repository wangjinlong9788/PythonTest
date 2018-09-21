#!/bin/python3

import os
import sys
import string
from queue import Queue





def fun(s):
    m=10**9+7
    a=100001
    l=len(s)
    f=0
    for i in range(l):
        f=f+ord(s[i])*a**(l-i-1)
       
    f=f%m
    return f

def solve(s, queries):
    #q = Queue()
    #ALPHABET = string.ascii_lowercase
    #shash = [0 for _ in ALPHABET]
    #for letter in s:
     #   shash[ord(letter)-ord(ALPHABET[0])] += 1
    

    #for i in range(len(shash)):
     #   while shash[i]>0:
      #      q.put(ALPHABET[i])
       #     shash[i]-=1
    #for


    snew=[]
    result=[]
    for start in range(len(s)):
        for finish in range(start, len(s)):
            temp=s[start:finish+1]
            if s[start:finish+1]==temp[::-1]:
                snew.append(temp)
            # initialize substring signature
            #signature = [0 for _ in ALPHABET]
            #for letter in s[start:finish+1]:
                #signature[ord(letter)-ord(ALPHABET[0])] += 1
    snew.sort()
    #print("snew",snew)
    #print(queries)
    #for i in range(len(snew)):
    for i in range(len(queries)):
        if queries[i]>len(snew):
            result.append(-1)
        else:
            f=fun(snew[queries[i]-1])
            result.append(f)
    return result
            
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    s = input()

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(s, queries)
    #print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
