#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:01:43 2021

SELECTION SORT

-First Step: Find smallest element and swap it with the element at index 0
-Second Step: In the remaining sublist extract the minimum element and swap it with
    the element at index 1

(better than bogo and bubble sort)

"""

def selection_sort(L):
        suffixSt = 0
        while suffixSt != len(L):
            for i in range(suffixSt, len(L)):
                if L[i] < L[suffixSt]:
                    L[suffixSt], L[i] = L[i], L[suffixSt]
                    print(L)
            suffixSt +=1
        print("It took Selection Sort " + str(suffixSt) + " iterations.")



test = [1,9,2,8,3,7,4,6,5,11,90,28,73,46,54]
selection_sort(test)