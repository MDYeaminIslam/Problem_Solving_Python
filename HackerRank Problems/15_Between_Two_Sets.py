#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a_factor = []
    b_factor = []
    common_factor = []
    max_len = len(a+b)
    for i in range(1,101):
        for number in a:
            if i % number == 0:
                a_factor.append(i)
    for i in range(1,101):
        for number in b:
            if number % i == 0:
                b_factor.append(i)
                
    temp_list = a_factor + b_factor
    
    for number in temp_list:
        if temp_list.count(number) == max_len:
            common_factor.append(number)
    return len(set(common_factor))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
