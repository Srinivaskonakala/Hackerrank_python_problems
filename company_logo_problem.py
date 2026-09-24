import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    count=Counter(s)
    sorted_count=sorted(count.items(),key=lambda x: (-x[1],x[0]))
    for char,number in sorted_count[:3]:
        print(char, number)