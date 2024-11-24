#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    # Print the array in reverse order
    print(" ".join(map(str, arr[::-1])))
