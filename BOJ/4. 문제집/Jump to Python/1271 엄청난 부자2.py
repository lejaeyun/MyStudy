import sys
input = sys.stdin.readline

n,m = map(int,input().split())
print(n//m)
print(n-((n//m)*m))
