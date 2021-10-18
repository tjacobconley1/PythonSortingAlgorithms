#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:37:40 2021

MONKEY SORT (bogo sort)

Shuffles a random list,
Checks if that list is in order,
if not then it randomly shuffles the list again


"""

import random


def bogo_sort(L):
    # to keep track of number of iterations
    count = 0

    while not is_sorted(L):
        random.shuffle(L)
        count +=1
        print(L)
    print("Bogo Sort took " + str(count) + " iterations to sort the list.")
    

def is_sorted(L):
    for i in range(len(L)):
        if L[i] > L[i+1]:
            return False
    return True

test = [1,9,2,8,3,7,4,6,5,11,90,28,73,46,54]

bogo_sort(test)