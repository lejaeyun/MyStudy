#17
def hanoi(n, start, via, des) :
    count = 0
    if n == 1 :
        return 1
    else :
        count += hanoi(n-1,start,des,via)
        count += 1
        count += hanoi(n-1,via,start,des)
    return count

n = int(input())
print(hanoi(n,1,2,3))
