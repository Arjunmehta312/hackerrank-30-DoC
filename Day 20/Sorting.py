#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    # Initialize total swap counter
    total_swaps = 0

    # Bubble Sort
    for i in range(n):
        numberOfSwaps = 0
        
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps += 1
        
        # Add to total swap counter
        total_swaps += numberOfSwaps
        
        # If no elements were swapped, array is sorted
        if numberOfSwaps == 0:
            break

    # Output results
    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
