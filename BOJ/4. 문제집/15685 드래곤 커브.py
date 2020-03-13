import sys
input = sys.stdin.readline

n = int(input())
result = 1000
arr = list()
for i in range(n) :
    arr.append(list(map(int,input().split())))
for i in range(n) :
    for j in range(n) :
        if i == j :
            continue
        else :
            sub = 
            if result > sub :
                result = sub

print(result)
