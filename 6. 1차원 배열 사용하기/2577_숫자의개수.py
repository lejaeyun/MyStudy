#https://www.acmicpc.net/problem/2577
import sys
input = sys.stdin.readline

def main() :
   A = int(input())
   B = int(input())
   C = int(input())
   mul = str(A*B*C)
   result = [0 for _ in range(10)]
   for i in mul :
      result[int(i)] += 1

   for i in result :
      print(i)
main()
