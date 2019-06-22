#https://www.acmicpc.net/problem/8958
import sys
input = sys.stdin.readline

def main() :
   N = int(input())
   for _ in range(N) :
      S = str(input())
      sum = 0
      index = 0
      for i in S :
         if i == "O" :
            index += 1
            sum += index
         else :
            index = 0
      print(sum)
      
main()
