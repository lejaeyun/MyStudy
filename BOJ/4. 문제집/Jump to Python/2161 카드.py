import sys
input = sys.stdin.readline
from collections import deque

arr = deque()
for i in range(1,int(input())+1) :
    arr.append(i)

while len(arr) != 1 :
    print(arr.popleft(), end = " ")
    arr.append(arr.popleft())
print(arr.popleft())
