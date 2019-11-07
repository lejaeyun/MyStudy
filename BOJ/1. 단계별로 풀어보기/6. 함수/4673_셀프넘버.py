#https://www.acmicpc.net/problem/2309
import sys
input = sys.stdin.readline

def main() :
   ll = [0 for _ in range(10000)]
   for i in range(10000) :
      s = 0
      s += i
      for j in str(i) :
         s += int(j)
      if s <= 10000 :
         ll[s-1] = 1
   for i in range(len(ll)) :
      if ll[i] == 0 :
         print(i+1)
   
main()
