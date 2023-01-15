#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # Get current ranked without duplicates
    ranked = list(dict.fromkeys(ranked))
    # Can also be done with:
    # ranked = list(set(ranked))
    # ranked.sort(reverse = True)
    
    # Assume the rank of the player is ranked the last at begining
    rank = len(ranked)
    # Assume the player maximum score 0 at begining
    ms = 0
    # create the list for the rank of the games which the player played
    r = list()
    for x in player:
        # if the current score greater than the maximum score scored
        if x > ms:
            # maximum score = current score
            ms = x
            # Find current rank
            while x >= ranked[rank-1] and rank != 0:
                rank -= 1
        # append crrent rank in list
        r.append(rank+1)
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()