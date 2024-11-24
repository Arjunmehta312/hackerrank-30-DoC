#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())  # Read the integer input
    binary_representation = bin(n)[2:]  # Convert to binary and strip the '0b' prefix
    
    # Split the binary representation by '0's and find the length of the longest group of '1's
    max_consecutive_ones = max(len(group) for group in binary_representation.split('0'))
    
    print(max_consecutive_ones)  # Print the result
