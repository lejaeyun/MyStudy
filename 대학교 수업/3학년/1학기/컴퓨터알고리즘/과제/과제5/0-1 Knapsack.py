
def knapSack(W, wt, val, n): 
    # 모든 List를 방문했을 때 or 무게가 다 찼을 때 0을 return
    if n < 0 or W == 0 : 
        return 0
    # 물건의 무게가 가방에 남은 무게보다 클 경우
    # 다른 물건으로 테스트. (이 부분이 교재에선 Promising)
    if (wt[n] > W): 
        return knapSack(W, wt, val, n-1)
    
    # 물건의 무게가 가방에 남은 무게보다 작을경우
    # 지금 물건의 가치 + 지금 물건을 넣은 후의 값 과
    # 지금 물건을 넣지 않고, 다른 물건을 넣었을 때의 값 중 큰 값을 리턴
    else:
        
        return max(val[n] + knapSack(W-wt[n], wt, val, n-1), 
                   knapSack(W, wt, val, n-1))
    
val = [20, 30, 35, 12 ,3] 
wt = [2, 5, 7, 3, 1] 
W = 9
n = len(val) 
print (knapSack(W, wt, val, n-1) )
