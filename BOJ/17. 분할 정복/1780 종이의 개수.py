import sys
input = sys.stdin.readline

def devide_arr(arr, n) :
    newarr = list()
    newn = n // 3
    point_arr = [0, newn, newn * n, newn * n + newn]
    for i in range(9) :
        point = point_arr[i]
        li = list()
        for r in range(newn) :
            lli = list()
            for c in range(newn) :
                lli.append(arr[point + n * r + c])
            li.extend(lli)
        newarr.append(li)
    return newarr

def check_rec(arr, n) :
    white = 0
    blue = 0
    
    if n == 1 :
        return 0, 0
    
    newn = n // 3
    newarr = devide_arr(arr, n)
    for l in newarr :
        if 0 not in l :
            blue += 1
            continue
        if 1 not in l :
            white += 1
            continue
        w,b = check_rec(l, newn)
        white, blue = white + w, blue + b
    
    return white, blue

def main() :
    array = list()
    num = int(input())
    for _ in range(num) :
        array.extend(list(map(int, input().split())))

    white, blue = check_rec(array, num)
    print(white)
    print(blue)

main()
