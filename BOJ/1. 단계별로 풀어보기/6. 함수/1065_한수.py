#https://www.acmicpc.net/problem/1065
import sys
input = sys.stdin.readline

def main() :
   N = int(input())
   if N < 100 :
      print(N)
      return
   else :
      count = 99
      for i in range(100,N+1) :
         a = i // 100
         b = (i//10) % 10
         c = i % 10
         if (a - b) == (b - c) :
            count += 1
   print(count)
   
   
main()
