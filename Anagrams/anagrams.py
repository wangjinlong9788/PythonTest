#!/bin/python3

import math
import os
import random
import re
import sys
import string


# Complete the sherlockAndAnagrams function below.
def anagrams(s1,s2):
    YN=True
    if len(s1)!=len(s2):
        YN=False
    dic={}
    
    for item1 in s1:
        dic[item1]=0
    for item1 in s1:
        dic[item1]+=1
    for item2 in s2:
        if item2 not in s1:
            dic[item2]=0
    for item2 in s2:
        dic[item2]-=1
    for i in range(len(s1)):
        if dic[s1[i]]!=0:
            YN=False
    return YN

def sherlockAndAnagrams_test(s):
   num=0
   pointer=False
   for k in range(1,len(s)):
       for i in range(len(s)-k):
           for j in range(len(s)-i-k):
               #print("%",s[i:i+k])
               #print(":",s[i+j+k:i+j:-1])
               #d1=[x for x in s[i:i+k] if x not in s[i+j+k:i+j:-1]]
               #d2=[x for x in s[i+j+k:i+j:-1] if x not in s[i:i+k]]
               #d=[x for x in s[i:i+k] if x in set(s[i+j+k:i+j:-1])]
               #string=''.join(str(y) for y in d)
               #if d1==[] and d2==[]:
               t=anagrams(s[i:i+k],s[i+j+1:i+j+k+1])
               if t:
               #if s[i:i+k]==s[i+j+k:i+j:-1] or s[i:i+k]==s[i+j+1:i+j+k+1]:
                   #print(s[i:i+k])
                   num+=1
                   #pointer=True
   
   #print("------------")
   #for j in range(i+k-1,len(s)-1):
   return num
   #if pointer:
    #   return num
   #else:
    #   return 0


#q = 1#int(raw_input())
def sherlockAndAnagrams(s):
    ALPHABET = string.ascii_lowercase
    #s ="abb"# raw_input()
    signatures = {}

    signature = [0 for _ in ALPHABET]
    for letter in s:
        signature[ord(letter)-ord(ALPHABET[0])] += 1
    print( signature)
    # iterate over all substrings of s
    for start in range(len(s)):
        for finish in range(start, len(s)):
            # initialize substring signature
            signature = [0 for _ in ALPHABET]
            for letter in s[start:finish+1]:
                signature[ord(letter)-ord(ALPHABET[0])] += 1
            # tuples are hashable in contrast to lists
            signature = tuple(signature)
            signatures[signature] = signatures.get(signature, 0) + 1

    res = 0
    #print(signatures)
    for count in signatures.values():
     #   print(count)
        res += count*(count-1)/2
    return(int(res))
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
