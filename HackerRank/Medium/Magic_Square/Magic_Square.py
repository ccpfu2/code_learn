#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # init the mincost at 15 * 3 =45
    mincost = 45
    # This is read by
    # r[0] r[7] r[6]
    # r[1]  x   r[5]
    # r[2] r[3] r[4]  
    r = s[0]+[s[1][2]]+s[2][::-1]+[s[1][0]]
    # one of the magic square
    c = [4,9,2,7,6,1,8,3]
    # i.e.:
    # 4 3 8
    # 9 5 1
    # 2 7 6 
    # Other Magic squares must be the roation or reflection of this Magic square
    
    for i in range(4):
        # compare with the possible magic square clockwise e.g.
        mincost = cal(r,c,mincost)
        # compare with the possible magic square anti-clockwise e.g.
        mincost = cal(r,[c[0]]+c[1:][::-1],mincost)
        # Rotate the possible magic square anti-clockwise
        c = c[2:]+c[0:2]

    # The middle one must be 5
    return mincost+abs(s[1][1]-5)

        
def cal(a,b,mincost):
    cost = 0
    for i in range(8):
        cost += abs(a[i]-b[i])
    if cost<mincost:
        return cost
    else:
        return mincost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()