#https://www.acmicpc.net/problem/2908
import sys
input = sys.stdin.readline

def main() :
   a,b = tuple(map(int, input().split()))
   aa = (a%10)*100 + ((a//10)%10) * 10 + ((a//100)%10)
   bb = (b%10)*100 + ((b//10)%10) * 10 + ((b//100)%10)
   if aa > bb :
      print(aa)
   else :
      print(bb)
   
main()
