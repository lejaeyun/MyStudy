import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    a,b = map(int,input().split())
    result = 1
    a = a % 10
    if a % 10 == 0 :
        print(10)
        continue
    for i in range(b) :
        result = result * a % 10
    print(result)
