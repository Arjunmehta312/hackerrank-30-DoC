#!/bin/python3

import os

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    max_bitwise = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            bitwise = i & j
            if max_bitwise < bitwise < K:
                max_bitwise = bitwise
            if max_bitwise == K - 1:
                return max_bitwise
    return max_bitwise

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
