#!/bin/python3

import math
import os
import random
import re
import sys
def isSteady(dic,n):
    for key in dic:
        if dic[key]>n/4.0:
             return False
    return True

# Complete the steadyGene function below.
def steadyGene(gene):
    dic={"A":0,"C":0,"G":0,"T":0}
    #for item in gene:
    #    dic[itme]=0
    n=len(gene)
    for item in gene:
        dic[item]+=1
    left = 0
    right = 0
    min0 =n+100;
    while right<n:
        dic[gene[right]]-=1
        right+=1
        while isSteady(dic,n):
            min0=min(min0,right-left)
            dic[gene[left]]+=1
            left+=1
    return min0



    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
