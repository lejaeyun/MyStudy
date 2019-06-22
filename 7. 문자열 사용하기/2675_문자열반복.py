#https://www.acmicpc.net/problem/2675
import sys
input = sys.stdin.readline

def main() :
   
   N = int(input())
   for _ in range(N) :
      st = input().split()
      n = int(st[0])
      s = st[1].split()[0]
      for j in s :
         print(j*n,end = "")
      print()
main()
