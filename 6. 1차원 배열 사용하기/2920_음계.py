#https://www.acmicpc.net/problem/2920
import sys
input = sys.stdin.readline

def main() :
   piano = list(map(int,input().split()))
   len = 9
   ascending = True
   descending = True
   for i in range(1,9) :
      if piano[i-1] != i :
         ascending = False
         
      if piano[i-1] != len-i :
         descending = False
         
      if ascending == False and descending == False :
         print("mixed")
         break
   if ascending == True :
      print("ascending")
   elif descending == True :
      print("descending")
      
main()
