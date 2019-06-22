#https://www.acmicpc.net/problem/10039
import sys
input = sys.stdin.readline

def main() :
   score = list()
   for _ in range(5) :
      s = int(input())
      if s < 40 :
         s = 40
      score.append(s)
   print(int(sum(score)/5))
      
main()
