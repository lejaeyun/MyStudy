import sys
input = sys.stdin.readline

for _ in range(3) :
    arr = list()
    for __ in range(int(input())) :
        arr.append(int(input()))
    s = sum(arr)
    if s == 0 :
        print(0)
    elif s > 0 :
        print('+')
    elif s < 0 :
        print('-')
