#https://www.acmicpc.net/problem/1157
import sys
input = sys.stdin.readline

def main() :
   alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   index = [0 for _ in range(26)]

   s = str(input().split()[0])
   ms = ""

   for i in range(len(s)) :
      ms += s[i].upper()

   for j in ms :
      index[alpha.index(j)] += 1

   le = []
   max = 0
   for i in range(len(index)) :
      j = index[i]
      if max == j :
         le.append(j)
      if max < j :
         le.clear()
         le.append(alpha[i])
         max = j
   
   if len(le) != 1 :
      print("?")
   else :
      print(le[0])
   
main()
