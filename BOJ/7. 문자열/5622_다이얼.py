#https://www.acmicpc.net/problem/5622
import sys
input = sys.stdin.readline

def main() :

   N = str(input().split()[0])
   alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   time = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
   t = 0
   for c in N :
      t += time[alpha.index(c)] + 1
   print(t)
   
   
main()
