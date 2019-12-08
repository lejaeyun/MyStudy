
for cnt in range(1, int(input())+1) :
    arr = list()
    for i in range(int(input())) :
        num = int(input())
        if num != 0 :
            arr.append(num)
        else :
            if arr :
                arr.pop()
    print("#"+str(cnt),sum(arr))
    
