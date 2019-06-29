#https://www.acmicpc.net/problem/2292
import sys
input = sys.stdin.readline

def main() :
   num = [1]
   start = 1
   plus = 6
   while True :
      start = start + plus
      num.append(start)
      plus = plus + 6
      if start > 1000000000 :
         num.append(start)
         break
   N = int(input())
   for i in range(len(num)) :
      if num[i] >= N :
         result = i+1
         break
   print(result)
   
main()
