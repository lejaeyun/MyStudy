# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    r,n = map(int, input().split())
    count = 1
    if n == r :
        print(1)
        continue
    for i in range(n-r+1, n + 1) :
        count = count * i
    for i in range(1, r + 1) :
        count = count // i
    print(count)
