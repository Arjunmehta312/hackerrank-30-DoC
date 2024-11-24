#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Read the integer input n
    n = int(input().strip())

    # Print the first 10 multiples of n
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")
