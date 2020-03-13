import sys
input = sys.stdin.readline
import itertools

n = int(input())
arr = list()
for i in range(n) :
    arr.append(list(map(int,input().split())))

combination_list = list()
tmplist = list(itertools.permutations([i for i in range(n)],n))

for i in tmplist :
    combination_list.append([i[0:n//2],i[n//2:]])

print(combination_list)

print(result)

