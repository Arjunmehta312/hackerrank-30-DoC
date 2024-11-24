#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    S = input().strip()
    
    try:
        # Attempt to convert the string to an integer
        print(int(S))
    except ValueError:
        # If conversion fails, output "Bad String"
        print("Bad String")
