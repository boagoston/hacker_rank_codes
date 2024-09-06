#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    response = 0
    for i,j in enumerate(s):
        if(i == len(s) - 1):
            break  
        if j == 'A' and s[i+1] == 'A':
            response += 1
        elif j == 'B' and s[i+1] == 'B':
            response += 1
                    
    return response





for i in range(q):
    s = input()
    print(alternatingCharacters(s))
    
    

