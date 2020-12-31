# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# Example



# There are  instances of ',  of '' and  of ''. For each query, add an element to the return array, .

# Function Description

# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

# matchingStrings has the following parameters:

# string strings[n] - an array of strings to search
# string queries[q] - an array of query strings
# Returns

# int[q]: an array of results for each query
# Input Format

# The first line contains and integer , the size of .
# Each of the next  lines contains a string .
# The next line contains , the size of .
# Each of the next  lines contains a string .

# Constraints



#  .

# Sample Input 1

# CopyDownload
# Array: strings
# aba
# baba
# aba
# xzxb

 



# Array: queries
# aba
# xzxb
# ab

 
# 4
# aba
# baba
# aba
# xzxb
# 3
# aba
# xzxb
# ab
# Sample Output 1

# 2
# 1
# 0
# Explanation 1

# Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string, and "ab" does not occur at all.


# Sample Input 2

# CopyDownload
# Array: strings
# def
# de
# fgh

 



# Array: queries
# de
# lmn
# fgh

 
# 3
# def
# de
# fgh
# 3
# de
# lmn
# fgh
# Sample Output 2

# 1
# 0
# 1

# Sample Input 3

# CopyDownload
# Array: strings
# abcde
# sdaklfj
# asdjf
# na
# basdn
# sdaklfj
# asdjf
# na
# asdjf
# na
# basdn
# sdaklfj
# asdjf

 



# Array: queries
# abcde
# sdaklfj
# asdjf
# na
# basdn

 
# 13
# abcde
# sdaklfj
# asdjf
# na
# basdn
# sdaklfj
# asdjf
# na
# asdjf
# na
# basdn
# sdaklfj
# asdjf
# 5
# abcde
# sdaklfj
# asdjf
# na
# basdn
# Sample Output 3

# 1
# 3
# 4
# 3
# 2



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    
    matches = 0
    outcome = []
    for chars in queries:
        for char in strings:
            if chars == char:
                matches += 1
        outcome.append(matches)
        matches = 0
        
    return outcome

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
