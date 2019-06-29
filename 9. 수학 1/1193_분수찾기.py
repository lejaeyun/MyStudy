#https://www.acmicpc.net/problem/1193
import sys
input = sys.stdin.readline

def main() :
   N = int(input())
   count = 1
   while N > count:
       N -= count
       count += 1
       
   if count % 2 == 1 :
      i = count - (N - 1)
      j = 1 + (N - 1)
   else :
      i = 1 + (N - 1)
      j = count - (N - 1)
      
   print(str(i) + "/" + str(j))
   
   
main()
