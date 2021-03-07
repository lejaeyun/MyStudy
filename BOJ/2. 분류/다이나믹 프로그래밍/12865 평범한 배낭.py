# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

def recursive_knapsack(items, remain_weight, index, cur_price):
    if index == len(items):
        return cur_price
    weight, price = items[index]
    if weight <= remain_weight:
        append = recursive_knapsack(items, remain_weight-weight, index+1, cur_price+price)
        not_append = recursive_knapsack(items, remain_weight, index+1, cur_price)
        return max(append, not_append)
    else:
        not_append = recursive_knapsack(items, remain_weight, index+1, cur_price)
        return not_append

def dp_knapsack(items, max_weight):
    dp = [[0 for _ in range(max_weight+1)] for _ in range(len(items)+1)]
    for i, item in enumerate(items, start=1):
        weight, price = item
        for j in range(1, max_weight+1):
            if weight <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+price)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][max_weight]

def main():
    N, K = map(int, input().strip().split())
    items = []
    for _ in range(N):
        items.append(list(map(int, input().strip().split())))
    items = sorted(items)
    # result = recursive_knapsack(items, K, 0, 0)
    result = dp_knapsack(items, K)
    print(result)

main()
