#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:10:33 2021

MERGE SORT

-If a list has a length of 0 or 1 then it's already sorted
-If a list has more than 1 element split it into 2 lists and sort each
-Merge Sorted Sublists
    >looks at first element of each and moves the smaller of the two
        to the end of the result list
    >when 1 list is empty just copy the rest of the other list

"""


# RECURSIVELY
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    while(i < len(left)):
        result.append(left[i])
        i +=1
    while(j < len(right)):
        result.append(right[j])
        j +=1
    print(result)
    return result 
        
test = [1,9,2,8,3,7,4,6,5,11,90,28,73,46,54]
merge_sort(test)