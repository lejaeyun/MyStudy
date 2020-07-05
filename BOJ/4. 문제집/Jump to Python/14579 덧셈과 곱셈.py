import sys
input = sys.stdin.readline

A,B = map(int,input().split())
s = 0
for i in range(1,A+1) :
    s = s + i

result = s
for i in range(A+1,B+1) :
    result = (result * (s + i)) % 14579
    s = s + i
    
print(result)
