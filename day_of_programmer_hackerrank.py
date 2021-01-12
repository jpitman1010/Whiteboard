#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    months = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sept': 30}
    month_nums =  {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', 'jul': '07', 'aug': '08', 'sept': '09'}
    if year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year %100 != 0):
            months['feb']= 29
        else:
            months['feb'] = 28
            
        
    elif year < 1918:
        if year % 4 == 0:
            months['feb'] = 29
        else:
            months['feb'] = 28
            
    day_of_programmer = 256        
    if year == 1918:
        day_of_programmer += 13
    for month in months.keys():
        if day_of_programmer - months[month] > 0:
            day_of_programmer -= months[month]
        else:
            print(f"{day_of_programmer}.{month_nums[month]}.{year}")
            return  f"{day_of_programmer}.{month_nums[month]}.{year}"
dayOfProgrammer(1918)

# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # year = int(input().strip())

    # result = dayOfProgrammer(year)

    # fptr.write(result + '\n')

    # fptr.close()
