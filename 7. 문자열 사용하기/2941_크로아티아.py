#https://www.acmicpc.net/problem/2941
import sys
input = sys.stdin.readline

def main() :

   N = str(input().split()[0])
   Croatia = ["c=","c-","z=","s=","nj","lj","d-","dz="]
   n = 0
   i = 0
   while True :
      if N[i:i+3] in Croatia :
         i += 3
         n += 1
      elif N[i:i+2] in Croatia :
         i += 2
         n += 1
      else :
         i += 1
         n += 1
      if i >= len(N) :
         break
   print(n)
      
main()
