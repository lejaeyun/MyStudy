import sys
input = sys.stdin.readline

n = int(input())
n = 1000 - n
result = 0
coin = [500,100,50,10,5,1]

for i in coin :
    
    if n >= i :
        coin_num = n // i
        result += coin_num
        n = n - coin_num * i
        
print(result)
