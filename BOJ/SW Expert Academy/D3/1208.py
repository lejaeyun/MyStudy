def main() : 
    for s in range(10) :
        num = int(input())
        arr = list(map(int, input().split()))
        for _ in range(num) :
            arr[arr.index(max(arr))] -= 1
            arr[arr.index(min(arr))] += 1
        result = max(arr) - min(arr)
        print("#"+ str(s+1) + " " + str(result))
        
main()
