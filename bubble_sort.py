#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:48:26 2021

BUBBLE SORT

-Compares consecutive pairs of elements
-Swaps element pairs such that the smalles is positioned first
-When end of a list is reached it starts again
-Stops when no more swaps have been made

"""

def bubble_sort(L):
    count = 0
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            count +=1
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp 
            print(L)
    print("It took Bubble Sort " + str(count) + " iteratrions.")
    
test = [1,9,2,8,3,7,4,6,5,11,90,28,73,46,54]

bubble_sort(test)