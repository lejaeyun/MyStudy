def main() : 
    for s in range(10) :
        num = int(input())
        arr = list(map(int, input().split()))
        result = 0
        for i in range(2, num - 2) :
            if arr[i] - arr[i-1] > 0 and arr[i] - arr[i-2] > 0 :
                if arr[i] - arr[i+1] > 0 and arr[i] - arr[i+2] > 0 :
                    result += min( arr[i] - arr[i-1], arr[i] - arr[i+1],  arr[i] - arr[i-2], arr[i] - arr[i+2] )
        print("#"+ str(s+1) + " " + str(result))
        
main()
